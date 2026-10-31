import LinkRoundedIcon from "@mui/icons-material/LinkRounded";
import ResourcePage from "../shared/ResourcePage";
import custodyService from "../../services/custodyService";

const config = {
  title: "Chain of custody",
  description: "Follow every evidence handoff with a traceable, time-stamped record.",
  icon: LinkRoundedIcon,
  service: custodyService,
  columns: [
    { key: "evidence_number", label: "Evidence ID", mono: true },
    { key: "action", label: "Event", status: true },
    { key: "from_user", label: "Released by" },
    { key: "to_user", label: "Received by" },
    { key: "location", label: "Location" },
    { key: "transferred_at", label: "Recorded" },
  ],
};

export default function CustodyPage() {
  return <ResourcePage config={config} />;
}
