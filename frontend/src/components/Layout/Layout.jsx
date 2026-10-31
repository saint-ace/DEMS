import { Outlet } from "react-router-dom";
import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

export default function Layout() {
  return (
    <div className="app-shell">
      <Sidebar />
      <div className="app-main">
        <Topbar />
        <main className="app-content">
          <Outlet />
        </main>
        <footer className="app-footer">
          <span>DEMS · Digital Evidence Management System</span>
          <span>Secure records. Trusted chain of custody.</span>
        </footer>
      </div>
    </div>
  );
}
