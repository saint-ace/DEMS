import { useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import ArrowForwardIcon from "@mui/icons-material/ArrowForward";
import FactCheckOutlinedIcon from "@mui/icons-material/FactCheckOutlined";
import LinkOutlinedIcon from "@mui/icons-material/LinkOutlined";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";
import StorageOutlinedIcon from "@mui/icons-material/StorageOutlined";
import VerifiedUserOutlinedIcon from "@mui/icons-material/VerifiedUserOutlined";
import VisibilityIcon from "@mui/icons-material/Visibility";
import VisibilityOffIcon from "@mui/icons-material/VisibilityOff";

import { useAuth } from "../../../context/AuthContext";
import "./LoginPage.css";

function DemsMark({ className = "" }) {
  return (
    <svg
      className={className}
      viewBox="0 0 72 84"
      fill="none"
      aria-hidden="true"
    >
      <path
        d="M36 3 67 15v25c0 18.8-12.8 31.7-31 41C17.8 71.7 5 58.8 5 40V15L36 3Z"
        stroke="currentColor"
        strokeWidth="4"
        strokeLinejoin="round"
      />
      <path
        d="M20 48V37c0-9 7.2-16.2 16-16.2S52 28 52 37v11M26 53V37a10 10 0 0 1 20 0v7M32 56V38a4 4 0 0 1 8 0v11M18 39c0-10.2 8.1-18.5 18-18.5M54 39c0-10.2-8.1-18.5-18-18.5M24 60c7.5 5.4 16.5 5.4 24 0M37 45c0 8-2.8 13.6-7.2 17.4"
        stroke="currentColor"
        strokeWidth="3"
        strokeLinecap="round"
      />
      <path
        d="m36 65 2.4-2.4"
        stroke="currentColor"
        strokeWidth="3"
        strokeLinecap="round"
      />
    </svg>
  );
}

const features = [
  { key: "secure-access", Icon: VerifiedUserOutlinedIcon, label: <>Secure<br />Access</> },
  { key: "evidence-management", Icon: StorageOutlinedIcon, label: <>Evidence<br />Management</> },
  { key: "chain-of-custody", Icon: LinkOutlinedIcon, label: <>Chain of<br />Custody</> },
  { key: "audit-tracking", Icon: FactCheckOutlinedIcon, label: <>Audit<br />Tracking</> },
];

export default function LoginPage() {
  const navigate = useNavigate();
  const { login, loading, isAuthenticated } = useAuth();
  const [formData, setFormData] = useState({ username: "", password: "" });
  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [rememberMe, setRememberMe] = useState(true);
  const [showPassword, setShowPassword] = useState(false);

  if (!loading && isAuthenticated) {
    return <Navigate to="/" replace />;
  }

  function handleChange(event) {
    const { name, value } = event.target;
    setFormData((previous) => ({ ...previous, [name]: value }));
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
    <main className="login-screen">
      <section className="login-showcase" aria-label="About DEMS">
        <div className="login-showcase__glow" />
        <div className="login-scene" aria-hidden="true">
          <div className="login-scene__screen">
            <div className="login-scene__toolbar" />
            <div className="login-scene__sidebar">
              <i /><i /><i /><i /><i />
            </div>
            <div className="login-scene__content">
              <div className="login-scene__fingerprint" />
              <div className="login-scene__network">
                <i /><i /><i /><i /><i />
              </div>
              <div className="login-scene__thumbs"><i /><i /><i /></div>
            </div>
          </div>
          <div className="login-scene__base" />
          <div className="login-scene__evidence" />
          <div className="login-scene__lens" />
        </div>

        <div className="login-showcase__content">
          <a className="dems-brand dems-brand--light" href="/login" aria-label="DEMS home">
            <DemsMark className="dems-brand__mark" />
            <span className="dems-brand__copy">
              <strong>DEMS</strong>
              <span>Digital Evidence<br />Management System</span>
            </span>
          </a>

          <div className="login-showcase__intro">
            <h1>Secure. Manage.<br /><span>Preserve.</span></h1>
            <p>
              The Digital Evidence Management System (DEMS) helps organizations
              collect, manage and track digital evidence with integrity,
              security and full chain of custody.
            </p>
          </div>

          <ul className="login-features">
            {features.map(({ key, Icon, label }) => (
              <li key={key}>
                <Icon aria-hidden="true" />
                <span>{label}</span>
              </li>
            ))}
          </ul>

          <p className="login-showcase__motto">Trust&nbsp; / &nbsp;Integrity&nbsp; / &nbsp;Justice</p>
        </div>
      </section>

      <section className="login-panel" aria-label="Sign in">
        <div className="login-panel__authorized">
          <LockOutlinedIcon aria-hidden="true" />
          <span>Authorized Personnel Only</span>
        </div>

        <div className="login-panel__content">
          <a className="dems-brand dems-brand--dark" href="/login" aria-label="DEMS home">
            <DemsMark className="dems-brand__mark" />
            <span className="dems-brand__copy">
              <strong>DEMS</strong>
              <span>Digital Evidence<br />Management System</span>
            </span>
          </a>

          <header className="login-heading">
            <h2>Welcome Back</h2>
            <p>Sign in to your account to access the DEMS platform.</p>
          </header>

          <form className="login-form" onSubmit={handleSubmit}>
            {error && (
              <div className="login-error" role="alert">
                {error}
              </div>
            )}

            <label htmlFor="username">Username</label>
            <div className="login-input">
              <PersonOutlinedIcon aria-hidden="true" />
              <input
                id="username"
                name="username"
                type="text"
                placeholder="Enter your username"
                autoComplete="username"
                value={formData.username}
                onChange={handleChange}
                required
              />
            </div>

            <label htmlFor="password">Password</label>
            <div className="login-input">
              <LockOutlinedIcon aria-hidden="true" />
              <input
                id="password"
                name="password"
                type={showPassword ? "text" : "password"}
                placeholder="Enter your password"
                autoComplete="current-password"
                value={formData.password}
                onChange={handleChange}
                required
              />
              <button
                className="login-input__toggle"
                type="button"
                aria-label={showPassword ? "Hide password" : "Show password"}
                onClick={() => setShowPassword((visible) => !visible)}
              >
                {showPassword ? <VisibilityOffIcon /> : <VisibilityIcon />}
              </button>
            </div>

            <div className="login-options">
              <label className="login-remember">
                <input
                  type="checkbox"
                  checked={rememberMe}
                  onChange={(event) => setRememberMe(event.target.checked)}
                />
                <span>Remember me</span>
              </label>
              <span className="login-forgot">Forgot your password?</span>
            </div>

            <button
              className="login-submit"
              type="submit"
              disabled={submitting || loading}
            >
              <span>{submitting ? "Signing in..." : "Sign In"}</span>
              {!submitting && <ArrowForwardIcon aria-hidden="true" />}
            </button>
          </form>

          <div className="login-divider">
            <span>Digital Evidence Management System</span>
          </div>

          <p className="login-legal">
            <VerifiedUserOutlinedIcon aria-hidden="true" />
            <span>
              This system is for authorized users only.
              <br />
              Unauthorized access is prohibited and may be subject to legal action.
            </span>
          </p>
        </div>
      </section>
    </main>
  );
}
