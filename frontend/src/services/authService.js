import api from "./api";

const authService = {
  async login(credentials) {
    const response = await api.post("auth/login/", credentials);
    const result = response.data.data || response.data;

    return {
      user: result.user,
      access: result.tokens?.access || result.access,
      refresh: result.tokens?.refresh || result.refresh,
    };
  },

  async getProfile() {
    const response = await api.get("auth/profile/");
    return response.data.data || response.data;
  },

  async logout(refresh) {
    const response = await api.post("auth/logout/", {
      refresh,
    });

    return response.data;
  },

  async refreshToken(refresh) {
    const response = await api.post("auth/refresh/", {
      refresh,
    });

    return response.data;
  },

  async updateProfile(profile) {
    const response = await api.patch("auth/profile/update/", profile);
    return response.data.data || response.data;
  },

  async changePassword(data) {
    const response = await api.post("auth/change-password/", data);
    return response.data;
  },

  async listUsers() {
    const response = await api.get("auth/users/");
    return response.data.results || response.data.data || response.data;
  },

  async register(data) {
    const response = await api.post("auth/register/", data);
    return response.data.data || response.data;
  },
};

export default authService;