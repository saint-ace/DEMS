import api from "../api/axios";

const authService = {
  async login(credentials) {
    const response = await api.post("auth/login/", credentials);
    return response.data;
  },

  async getProfile() {
    const response = await api.get("auth/profile/");
    return response.data;
  },

  async logout(refresh) {
    const response = await api.post("auth/logout/", {
      refresh,
    });

    return response.data;
  },

  async refreshToken(refresh) {
    const response = await api.post("auth/token/refresh/", {
      refresh,
    });

    return response.data;
  },
};

export default authService;