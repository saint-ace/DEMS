import FingerprintRoundedIcon from "@mui/icons-material/FingerprintRounded";
import ResourcePage from "../shared/ResourcePage";
import evidenceService from "../../services/evidenceService";

const config = {
  title: "Digital evidence",
  description: "Track collected files, verification status, and their case of record.",
  icon: FingerprintRoundedIcon,
  service: evidenceService,
  columns: [
    { key: "evidence_number", label: "Evidence ID", mono: true },
    { key: "title", label: "Evidence item" },
    { key: "evidence_type", label: "Format" },
    { key: "case_number", label: "Case", mono: true },
    { key: "collected_by", label: "Collected by" },
    { key: "status", label: "Status", status: true },
    {
      key: "verified",
      label: "Integrity",
      render: (value) => (
        <span className={`status-pill ${value ? "is-positive" : "is-progress"}`}>
          <i />{value ? "Verified" : "Pending"}
        </span>
      ),
    },
  ],
};

export default function EvidencePage() {
  return <ResourcePage config={config} />;
}
