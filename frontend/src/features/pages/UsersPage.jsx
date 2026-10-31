import PeopleAltRoundedIcon from "@mui/icons-material/PeopleAltRounded";
import ResourcePage from "../shared/ResourcePage";
import userService from "../../services/userService";

const config = {
  title: "People & access",
  description: "See the people entrusted with investigations and digital evidence.",
  icon: PeopleAltRoundedIcon,
  service: userService,
  columns: [
    { key: "username", label: "Username", mono: true },
    {
      key: "name",
      label: "Name",
      value: (user) => [user.first_name, user.last_name].filter(Boolean).join(" "),
    },
    { key: "email", label: "Email" },
    { key: "department", label: "Department" },
    { key: "role", label: "Role" },
    {
      key: "is_active",
      label: "Account",
      render: (value) => (
        <span className={`status-pill ${value ? "is-positive" : "is-negative"}`}>
          <i />{value ? "Active" : "Inactive"}
        </span>
      ),
    },
  ],
};

export default function UsersPage() {
  return <ResourcePage config={config} />;
}
