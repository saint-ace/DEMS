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

  const logout = useCallback(async () => {
    try {
      const refresh = localStorage.getItem("refresh");

      if (refresh && typeof authService.logout === "function") {
        await authService.logout(refresh);
      }
    } catch (error) {
      console.error("Logout request failed:", error);
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
      console.error("Unable to load the user profile:", error);

      localStorage.removeItem("access");
      localStorage.removeItem("refresh");

      setUser(null);
      setIsAuthenticated(false);
    } finally {
      setLoading(false);
    }
  }, []);

  const login = async (credentials) => {
    const response = await authService.login(credentials);

    const result = response.data ?? response;
    const tokens = result.tokens ?? result;

    const access = tokens.access;
    const refresh = tokens.refresh;

    if (!access) {
      throw new Error(
        "The login response did not contain an access token."
      );
    }

    localStorage.setItem("access", access);

    if (refresh) {
      localStorage.setItem("refresh", refresh);
    }

    try {
      const profile =
        result.user ?? (await authService.getProfile());

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
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error(
      "useAuth must be used inside an AuthProvider."
    );
  }

  return context;
}