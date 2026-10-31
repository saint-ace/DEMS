import api from "./api";

const auditService = {
  async list(params = {}) {
    const { data } = await api.get("audit/", { params });
    return data.results || data;
  },

  async get(id) {
    const { data } = await api.get(`audit/${id}/`);
    return data;
  },
};

export default auditService;
