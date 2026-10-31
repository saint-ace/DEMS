import axios from "axios";

const configuredBaseUrl =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000/api/";
const apiBaseUrl = configuredBaseUrl.endsWith("/")
  ? configuredBaseUrl
  : `${configuredBaseUrl}/`;

const api = axios.create({
  baseURL: apiBaseUrl,
  timeout: 30000,
  headers: {
    "Content-Type": "application/json",
  },
});

let refreshRequest;

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const request = error.config;
    const url = request?.url || "";
    const isAuthRequest =
      url.includes("auth/login/") ||
      url.includes("auth/refresh/") ||
      url.includes("auth/logout/");

    if (error.response?.status !== 401 || !request || request._retry || isAuthRequest) {
      return Promise.reject(error);
    }

    const refresh = localStorage.getItem("refresh");
    if (!refresh) return Promise.reject(error);

    request._retry = true;

    try {
      if (!refreshRequest) {
        refreshRequest = axios
          .post(`${apiBaseUrl}auth/refresh/`, { refresh }, { timeout: api.defaults.timeout })
          .then(({ data }) => {
            if (!data.access) {
              throw new Error("The refresh endpoint did not return an access token.");
            }
            localStorage.setItem("access", data.access);
            if (data.refresh) localStorage.setItem("refresh", data.refresh);
            return data.access;
          })
          .catch((refreshError) => {
            localStorage.removeItem("access");
            localStorage.removeItem("refresh");
            throw refreshError;
          })
          .finally(() => {
            refreshRequest = undefined;
          });
      }

      const access = await refreshRequest;
      request.headers = request.headers || {};
      request.headers.Authorization = `Bearer ${access}`;
      return api(request);
    } catch (refreshError) {
      return Promise.reject(refreshError);
    }
  }
);

export default api;
