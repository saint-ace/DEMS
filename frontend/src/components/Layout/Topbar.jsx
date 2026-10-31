import { useNavigate } from "react-router-dom";
import NotificationsNoneRoundedIcon from "@mui/icons-material/NotificationsNoneRounded";
import LogoutRoundedIcon from "@mui/icons-material/LogoutRounded";
import { useAuth } from "../../context/AuthContext";

export default function Topbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const displayName = user?.first_name || user?.username || "DEMS user";
  const initials = [user?.first_name?.[0], user?.last_name?.[0]]
    .filter(Boolean)
    .join("")
    .toUpperCase() || displayName.slice(0, 1).toUpperCase();

  async function handleLogout() {
    await logout();
    navigate("/login", { replace: true });
  }

  return (
    <header className="app-topbar">
      <div className="app-topbar__breadcrumb"><span>Workspace</span><i>/</i><strong>Evidence operations</strong></div>
      <div className="app-topbar__actions">
        <span className="app-topbar__secure"><i /> Secure connection</span>
        <button className="app-topbar__icon" type="button" aria-label="Notifications" title="Notifications">
          <NotificationsNoneRoundedIcon />
          <i />
        </button>
        <div className="app-topbar__user">
          <span className="app-topbar__avatar">{initials}</span>
          <span className="app-topbar__user-copy"><strong>{displayName}</strong><small>{user?.role || "Authorized personnel"}</small></span>
        </div>
        <button className="app-topbar__logout" onClick={handleLogout} type="button" title="Sign out" aria-label="Sign out">
          <LogoutRoundedIcon />
        </button>
      </div>
    </header>
  );
}
