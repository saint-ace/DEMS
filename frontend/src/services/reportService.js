import api from "./api";

const reportService = {
  async list() {
    const { data } = await api.get("reports/");
    return data.results || data;
  },

  async get(id) {
    const { data } = await api.get(`reports/${id}/`);
    return data.data || data;
  },

  async generate(payload) {
    const { data } = await api.post("reports/generate/", payload);
    return data.data || data;
  },

  async remove(id) {
    await api.delete(`reports/${id}/delete/`);
  },
};

export default reportService;