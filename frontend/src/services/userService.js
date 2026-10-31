import authService from "./authService";

const userService = {
  list: authService.listUsers,
  getProfile: authService.getProfile,
  updateProfile: authService.updateProfile,
  create: authService.register,
};

export default userService;