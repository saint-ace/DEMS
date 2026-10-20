import api from "./api";

const AUTH_BASE = "/auth";

const authService = {
  async login(credentials) {
    const response = await api.post(
      `${AUTH_BASE}/login/`,
      credentials
    );

    return response.data;
  },

  async logout(refreshToken) {
    const response = await api.post(
      `${AUTH_BASE}/logout/`,
      {
        refresh: refreshToken,
      }
    );

    return response.data;
  },

  async refresh(refreshToken) {
    const response = await api.post(
      `${AUTH_BASE}/refresh/`,
      {
        refresh: refreshToken,
      }
    );

    return response.data;
  },

  async getProfile() {
    const response = await api.get(
      `${AUTH_BASE}/profile/`
    );

    return response.data;
  },

  async changePassword(data) {
    const response = await api.post(
      `${AUTH_BASE}/change-password/`,
      data
    );

    return response.data;
  },

  async forgotPassword(email) {
    const response = await api.post(
      `${AUTH_BASE}/forgot-password/`,
      {
        email,
      }
    );

    return response.data;
  },

  async resetPassword(data) {
    const response = await api.post(
      `${AUTH_BASE}/reset-password/`,
      data
    );

    return response.data;
  },
};

export default authService;