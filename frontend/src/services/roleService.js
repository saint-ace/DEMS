import api from "./api";

const roleService = {
  async list() {
    const { data } = await api.get("rbac/roles/");
    return data.results || data;
  },

  async permissions() {
    const { data } = await api.get("rbac/permissions/");
    return data.results || data;
  },

  async assignments() {
    const { data } = await api.get("rbac/assignments/");
    return data.results || data;
  },
};

export default roleService;