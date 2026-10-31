import FolderOpenRoundedIcon from "@mui/icons-material/FolderOpenRounded";
import ResourcePage from "../shared/ResourcePage";
import caseService from "../../services/caseService";

const config = {
  title: "Case management",
  description: "A clear view of active investigations, ownership, and case priorities.",
  icon: FolderOpenRoundedIcon,
  service: caseService,
  columns: [
    { key: "case_number", label: "Case reference", mono: true },
    { key: "title", label: "Investigation" },
    { key: "case_type", label: "Case type" },
    { key: "status", label: "Status", status: true },
    { key: "priority", label: "Priority", status: true },
    { key: "lead_investigator", label: "Lead investigator" },
    { key: "date_opened", label: "Opened" },
  ],
};

export default function CasesPage() {
  return <ResourcePage config={config} />;
}
