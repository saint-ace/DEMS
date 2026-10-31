import api from "./api";

const custodyService = {
  async list(params = {}) {
    const { data } = await api.get("custody/", { params });
    return data.results || data;
  },

  async get(id) {
    const { data } = await api.get(`custody/${id}/`);
    return data.data || data;
  },

  async transfer(payload) {
    const { data } = await api.post("custody/transfer/", payload);
    return data.data || data;
  },
};

export default custodyService;