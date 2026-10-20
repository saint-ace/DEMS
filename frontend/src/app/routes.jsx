import { Routes, Route } from "react-router-dom";

import ProtectedRoute from "./ProtectedRoute";

import AppLayout from "../layouts/AppLayout";

import LoginPage from "../features/auth/pages/LoginPage";
import DashboardPage from "../features/dashboard/pages/DashboardPage";

export default function AppRoutes() {
  return (
    <Routes>
      {/* Public routes */}
      <Route path="/login" element={<LoginPage />} />

      {/* Protected routes */}
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <AppLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<DashboardPage />} />
      </Route>

      {/* Fallback route */}
      <Route path="*" element={<div>Page not found.</div>} />
    </Routes>
  );
}