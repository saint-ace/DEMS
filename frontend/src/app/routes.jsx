import { lazy, Suspense } from "react";
import { Routes, Route } from "react-router-dom";

import ProtectedRoute from "./ProtectedRoute";

import LoginPage from "../features/auth/pages/LoginPage";

const AppLayout = lazy(() => import("../components/Layout/Layout"));
const Dashboard = lazy(() => import("../features/dashboard/Dashboard"));
const CasesPage = lazy(() => import("../features/pages/CasesPage"));
const EvidencePage = lazy(() => import("../features/pages/EvidencePage"));
const CustodyPage = lazy(() => import("../features/pages/CustodyPage"));
const ReportsPage = lazy(() => import("../features/pages/ReportsPage"));
const AuditPage = lazy(() => import("../features/pages/AuditPage"));
const UsersPage = lazy(() => import("../features/pages/UsersPage"));
const RolesPage = lazy(() => import("../features/pages/RolesPage"));
const SettingsPage = lazy(() => import("../features/pages/SettingsPage"));

export default function AppRoutes() {
  return (
    <Routes>
      {/* Public routes */}
      <Route path="/login" element={<LoginPage />} />

      {/* Protected routes */}
      <Route
        path="/"
        element={
          <Suspense fallback={<div className="app-loading">Opening your secure workspace…</div>}>
            <ProtectedRoute>
              <AppLayout />
            </ProtectedRoute>
          </Suspense>
        }
      >
        <Route index element={<Dashboard />} />
        <Route path="cases" element={<CasesPage />} />
        <Route path="evidence" element={<EvidencePage />} />
        <Route path="custody" element={<CustodyPage />} />
        <Route path="reports" element={<ReportsPage />} />
        <Route path="audit" element={<AuditPage />} />
        <Route path="users" element={<UsersPage />} />
        <Route path="roles" element={<RolesPage />} />
        <Route path="settings" element={<SettingsPage />} />
      </Route>

      {/* Fallback route */}
      <Route path="*" element={<div>Page not found.</div>} />
    </Routes>
  );
}