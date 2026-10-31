import { Link, NavLink } from "react-router-dom";
import VerifiedUserRoundedIcon from "@mui/icons-material/VerifiedUserRounded";
import menuItems from "./MenuItems";

export default function Sidebar() {
  return (
    <aside className="app-sidebar">
      <Link className="app-sidebar__brand" to="/" aria-label="DEMS dashboard">
        <span className="app-sidebar__shield"><VerifiedUserRoundedIcon /></span>
        <span><strong>DEMS</strong><small>Evidence intelligence</small></span>
      </Link>
      <span className="app-sidebar__section">WORKSPACE</span>
      <nav className="app-nav" aria-label="Main navigation">
        {menuItems.map(({ text, icon, path }) => (
          <NavLink
            key={path}
            to={path}
            end={path === "/"}
            className={({ isActive }) => `app-nav__link${isActive ? " is-active" : ""}`}
          >
            <span className="app-nav__icon">{icon}</span>
            <span>{text}</span>
            <span className="app-nav__active-mark" />
          </NavLink>
        ))}
      </nav>
      <div className="app-sidebar__security">
        <span className="app-sidebar__security-icon"><VerifiedUserRoundedIcon /></span>
        <div><strong>Secure workspace</strong><span>Access is monitored</span></div>
        <i />
      </div>
      <div className="app-sidebar__footer">TRUST <i /> INTEGRITY <i /> JUSTICE</div>
    </aside>
  );
}
