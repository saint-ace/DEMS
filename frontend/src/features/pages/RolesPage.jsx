import AdminPanelSettingsRoundedIcon from "@mui/icons-material/AdminPanelSettingsRounded";
import ResourcePage from "../shared/ResourcePage";
import roleService from "../../services/roleService";

const config = {
  title: "Roles & permissions",
  description: "Understand how access is organized across the DEMS platform.",
  icon: AdminPanelSettingsRoundedIcon,
  service: roleService,
  columns: [
    { key: "name", label: "Role" },
    { key: "description", label: "Description" },
  ],
};

export default function RolesPage() {
  return <ResourcePage config={config} />;
}
