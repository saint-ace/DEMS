import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useState,
} from "react";

import authService from "../services/authService";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
const [user, setUser] = useState(null);
const [loading, setLoading] = useState(true);
const [isAuthenticated, setIsAuthenticated] = useState(
    Boolean(localStorage.getItem("access"))
);
const login = async (credentials) => {
  const data = await authService.login(credentials);

  localStorage.setItem("access", data.access);
  localStorage.setItem("refresh", data.refresh);

  try {
    const profile = await authService.getProfile();

    setUser(profile);
    setIsAuthenticated(true);

    return profile;
  } catch (error) {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");

    setUser(null);
    setIsAuthenticated(false);

    throw error;
  }
};

  const logout = useCallback(async () => {
    try {
      const refresh = localStorage.getItem("refresh");

      if (refresh) {
        await authService.logout(refresh);
      }
    } catch (error) {
      console.error(error);
    } finally {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");

  setUser(null);
  setIsAuthenticated(false);
}
  }, []);

  const refreshProfile = useCallback(async () => {
  try {
    const profile = await authService.getProfile();

    setUser(profile);
    setIsAuthenticated(true);
  } catch (error) {
    await logout();
  } finally {
    setLoading(false);
  }
}, [logout]);

  useEffect(() => {
    if (localStorage.getItem("access")) {
      refreshProfile();
    } else {
      setLoading(false);
    }
  }, [refreshProfile]);

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        login,
        logout,
        refreshProfile,
        isAuthenticated,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}