import { useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";

import { useAuth } from "../../../context/AuthContext";

export default function LoginPage() {
  const navigate = useNavigate();

  const {
    login,
    loading,
    isAuthenticated,
  } = useAuth();

  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  if (!loading && isAuthenticated) {
    return <Navigate to="/" replace />;
  }

  function handleChange(event) {
    const { name, value } = event.target;

    setFormData((previous) => ({
      ...previous,
      [name]: value,
    }));
  }

  async function handleSubmit(event) {
    event.preventDefault();

    setError("");
    setSubmitting(true);

    try {
    await login({
        username: formData.username,
        password: formData.password,
    });
      navigate("/", { replace: true });
    } catch (err) {
      setError(
        err?.response?.data?.detail ||
          err?.response?.data?.message ||
          "Login failed. Please check your credentials and try again."
      );
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div className="login-page">
      <form className="login-form" onSubmit={handleSubmit}>
        <h1>DEMS</h1>
        <h2>Sign in</h2>

        <p>Digital Evidence Management System</p>

        {error && (
          <div className="login-error" role="alert">
            {error}
          </div>
        )}

        <label htmlFor="username">Username</label>
        <input
          id="username"
          name="username"
          type="text"
          autoComplete="username"
          value={formData.username}
          onChange={handleChange}
          required
        />

        <label htmlFor="password">Password</label>
        <input
          id="password"
          name="password"
          type="password"
          autoComplete="current-password"
          value={formData.password}
          onChange={handleChange}
          required
        />

        <button type="submit" disabled={submitting || loading}>
          {submitting ? "Signing in..." : "Sign in"}
        </button>
      </form>
    </div>
  );
}