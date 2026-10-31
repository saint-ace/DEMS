import { useEffect, useState } from "react";
import ManageAccountsRoundedIcon from "@mui/icons-material/ManageAccountsRounded";
import PasswordRoundedIcon from "@mui/icons-material/PasswordRounded";
import authService from "../../services/authService";
import { useAuth } from "../../context/AuthContext";

const emptyProfile = { first_name: "", last_name: "", phone_number: "" };
const emptyPassword = { old_password: "", new_password: "", confirm_password: "" };

function getErrorMessage(error) {
  const data = error?.response?.data;
  if (typeof data === "string") return data;
  if (data?.detail) return data.detail;
  if (data && typeof data === "object") {
    return Object.values(data).flat().join(" ");
  }
  return error?.message || "Something went wrong. Please try again.";
}

export default function SettingsPage() {
  const { user, refreshProfile } = useAuth();
  const [profile, setProfile] = useState(emptyProfile);
  const [password, setPassword] = useState(emptyPassword);
  const [loading, setLoading] = useState(true);
  const [savingProfile, setSavingProfile] = useState(false);
  const [savingPassword, setSavingPassword] = useState(false);
  const [notice, setNotice] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    let active = true;
    authService.getProfile()
      .then((data) => {
        if (!active) return;
        setProfile({
          first_name: data.first_name || "",
          last_name: data.last_name || "",
          phone_number: data.phone_number || "",
        });
      })
      .catch((requestError) => {
        if (active) setError(getErrorMessage(requestError));
      })
      .finally(() => {
        if (active) setLoading(false);
      });
    return () => { active = false; };
  }, []);

  function updateField(setter) {
    return (event) => {
      const { name, value } = event.target;
      setter((previous) => ({ ...previous, [name]: value }));
    };
  }

  async function saveProfile(event) {
    event.preventDefault();
    setError("");
    setNotice("");
    setSavingProfile(true);
    try {
      await authService.updateProfile(profile);
      await refreshProfile();
      setNotice("Profile details saved.");
    } catch (requestError) {
      setError(getErrorMessage(requestError));
    } finally {
      setSavingProfile(false);
    }
  }

  async function changePassword(event) {
    event.preventDefault();
    setError("");
    setNotice("");
    setSavingPassword(true);
    try {
      await authService.changePassword(password);
      setPassword(emptyPassword);
      setNotice("Your password has been updated.");
    } catch (requestError) {
      setError(getErrorMessage(requestError));
    } finally {
      setSavingPassword(false);
    }
  }

  return (
    <section className="resource-page">
      <header className="workspace-hero">
        <div className="workspace-hero__copy">
          <div className="workspace-eyebrow"><span className="workspace-eyebrow__dot" />ACCOUNT CONTROL</div>
          <h1>Settings</h1>
          <p>Keep your profile current and protect access to your account.</p>
        </div>
        <div className="workspace-hero__art" aria-hidden="true">
          <span className="workspace-hero__ring workspace-hero__ring--outer" />
          <span className="workspace-hero__ring workspace-hero__ring--inner" />
          <span className="workspace-hero__icon"><ManageAccountsRoundedIcon /></span>
          <span className="workspace-hero__spark workspace-hero__spark--one" />
          <span className="workspace-hero__spark workspace-hero__spark--two" />
        </div>
      </header>

      {error && <div className="resource-error" role="alert">{error}</div>}
      {notice && <div className="resource-notice" role="status">{notice}</div>}

      <div className="settings-grid">
        <form className="settings-card" onSubmit={saveProfile}>
          <div className="settings-card__heading">
            <span className="settings-card__icon"><ManageAccountsRoundedIcon /></span>
            <div>
              <h2>Personal details</h2>
              <p>Update the profile details associated with your account.</p>
            </div>
          </div>
          <div className="settings-identity">
            <span className="settings-avatar">
              {(user?.first_name || user?.username || "U").slice(0, 1).toUpperCase()}
            </span>
            <div>
              <strong>{user?.first_name || user?.last_name
                ? `${user.first_name || ""} ${user.last_name || ""}`.trim()
                : user?.username || "Signed-in user"}</strong>
              <span>{user?.email || "Authorized DEMS account"}</span>
            </div>
            <span className="status-pill is-positive"><i />Active</span>
          </div>
          <div className="settings-fields">
            <label>
              First name
              <input
                name="first_name"
                value={profile.first_name}
                onChange={updateField(setProfile)}
                autoComplete="given-name"
                disabled={loading}
              />
            </label>
            <label>
              Last name
              <input
                name="last_name"
                value={profile.last_name}
                onChange={updateField(setProfile)}
                autoComplete="family-name"
                disabled={loading}
              />
            </label>
            <label className="settings-fields__full">
              Phone number
              <input
                name="phone_number"
                value={profile.phone_number}
                onChange={updateField(setProfile)}
                autoComplete="tel"
                disabled={loading}
              />
            </label>
          </div>
          <button className="primary-action" type="submit" disabled={loading || savingProfile}>
            {savingProfile ? "Saving…" : "Save profile"}
          </button>
        </form>

        <form className="settings-card" onSubmit={changePassword}>
          <div className="settings-card__heading">
            <span className="settings-card__icon settings-card__icon--violet"><PasswordRoundedIcon /></span>
            <div>
              <h2>Change password</h2>
              <p>Use a strong password you have not used elsewhere.</p>
            </div>
          </div>
          <div className="settings-fields settings-fields--single">
            <label>
              Current password
              <input
                type="password"
                name="old_password"
                value={password.old_password}
                onChange={updateField(setPassword)}
                autoComplete="current-password"
                required
              />
            </label>
            <label>
              New password
              <input
                type="password"
                name="new_password"
                value={password.new_password}
                onChange={updateField(setPassword)}
                autoComplete="new-password"
                minLength={8}
                required
              />
            </label>
            <label>
              Confirm new password
              <input
                type="password"
                name="confirm_password"
                value={password.confirm_password}
                onChange={updateField(setPassword)}
                autoComplete="new-password"
                minLength={8}
                required
              />
            </label>
          </div>
          <button className="primary-action primary-action--violet" type="submit" disabled={savingPassword}>
            {savingPassword ? "Updating…" : "Update password"}
          </button>
        </form>
      </div>
    </section>
  );
}
