import api from "./api";

const evidenceService = {
  async list(params = {}) {
    const { data } = await api.get("evidence/", { params });
    return data.results || data;
  },

  async get(id) {
    const { data } = await api.get(`evidence/${id}/`);
    return data.data || data;
  },

  async upload(payload) {
    const { data } = await api.post("evidence/upload/", payload, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return data.data || data;
  },
};

export default evidenceService;