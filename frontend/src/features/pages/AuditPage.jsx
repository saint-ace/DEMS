import HistoryRoundedIcon from "@mui/icons-material/HistoryRounded";
import ResourcePage from "../shared/ResourcePage";
import auditService from "../../services/auditService";

const config = {
  title: "Audit trail",
  description: "An accountable timeline of activity across your evidence workspace.",
  icon: HistoryRoundedIcon,
  columns: [
    { key: "created_at", label: "Timestamp" },
    { key: "username", label: "User" },
    { key: "module", label: "Area" },
    { key: "action", label: "Action", status: true },
    { key: "object_type", label: "Record type" },
    { key: "description", label: "Activity" },
  ],
  service: auditService,
};

export default function AuditPage() {
  return <ResourcePage config={config} />;
}
