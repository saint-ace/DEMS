import api from "./api";

const caseService = {
  async list(params = {}) {
    const { data } = await api.get("cases/", { params });
    return data.results || data;
  },

  async get(id) {
    const { data } = await api.get(`cases/${id}/`);
    return data.data || data;
  },

  async create(payload) {
    const { data } = await api.post("cases/create/", payload);
    return data.data || data;
  },
};

export default caseService;