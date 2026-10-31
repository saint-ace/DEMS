import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import ArrowOutwardRoundedIcon from "@mui/icons-material/ArrowOutwardRounded";
import AssessmentRoundedIcon from "@mui/icons-material/AssessmentRounded";
import FolderOpenRoundedIcon from "@mui/icons-material/FolderOpenRounded";
import FingerprintRoundedIcon from "@mui/icons-material/FingerprintRounded";
import HistoryRoundedIcon from "@mui/icons-material/HistoryRounded";
import LinkRoundedIcon from "@mui/icons-material/LinkRounded";
import caseService from "../../services/caseService";
import evidenceService from "../../services/evidenceService";
import custodyService from "../../services/custodyService";
import auditService from "../../services/auditService";
import { useAuth } from "../../context/AuthContext";

const summaryItems = [
  { key: "cases", label: "Active cases", detail: "Investigation records", Icon: FolderOpenRoundedIcon, to: "/cases", accent: "blue" },
  { key: "evidence", label: "Evidence items", detail: "Digital assets managed", Icon: FingerprintRoundedIcon, to: "/evidence", accent: "cyan" },
  { key: "custody", label: "Custody events", detail: "Chain-of-custody records", Icon: LinkRoundedIcon, to: "/custody", accent: "violet" },
];

function readableDate(value) {
  if (!value) return "Recently";
  const date = new Date(value);
  return Number.isNaN(date.getTime())
    ? "Recently"
    : new Intl.DateTimeFormat(undefined, { dateStyle: "medium" }).format(date);
}

export default function Dashboard() {
  const { user } = useAuth();
  const [snapshot, setSnapshot] = useState({ cases: null, evidence: null, custody: null, audit: null });
  const [errors, setErrors] = useState([]);

  useEffect(() => {
    let active = true;
    const requests = [
      ["cases", caseService.list()],
      ["evidence", evidenceService.list()],
      ["custody", custodyService.list()],
      ["audit", auditService.list()],
    ];
    Promise.all(requests.map(async ([key, request]) => {
      try {
        const result = await request;
        if (!Array.isArray(result)) throw new Error("Unexpected API response.");
        return { key, result };
      } catch (error) {
        return { key, error };
      }
    })).then((results) => {
      if (!active) return;
      const next = { cases: false, evidence: false, custody: false, audit: false };
      const failed = [];
      results.forEach(({ key, result, error }) => {
        if (error) failed.push(key);
        else next[key] = result;
      });
      setSnapshot(next);
      setErrors(failed);
    });
    return () => { active = false; };
  }, []);

  const firstName = user?.first_name || user?.username || "there";
  const recentActivity = (snapshot.audit || []).slice(0, 4);

  return (
    <section className="dashboard-page">
      <header className="dashboard-hero">
        <div className="dashboard-hero__copy">
          <span className="dashboard-kicker"><i /> DIGITAL EVIDENCE MANAGEMENT SYSTEM</span>
          <h1>Your workspace,<br /><span>in focus.</span></h1>
          <p>One secure place to follow investigations, safeguard evidence, and preserve every link in the chain.</p>
          <div className="dashboard-hero__actions">
            <Link className="dashboard-primary-link" to="/cases">Explore cases <ArrowOutwardRoundedIcon /></Link>
            <Link className="dashboard-secondary-link" to="/evidence">View evidence</Link>
          </div>
        </div>
        <div className="dashboard-hero__visual" aria-hidden="true">
          <div className="dashboard-orbit dashboard-orbit--one" />
          <div className="dashboard-orbit dashboard-orbit--two" />
          <div className="dashboard-core"><FingerprintRoundedIcon /></div>
          <span className="dashboard-orbit-dot dashboard-orbit-dot--one" />
          <span className="dashboard-orbit-dot dashboard-orbit-dot--two" />
          <span className="dashboard-orbit-dot dashboard-orbit-dot--three" />
          <div className="dashboard-float-card dashboard-float-card--top"><span>INTEGRITY</span><strong>Verified</strong><i /></div>
          <div className="dashboard-float-card dashboard-float-card--bottom"><span>CHAIN OF CUSTODY</span><strong>Always traceable</strong></div>
        </div>
        <p className="dashboard-hello">Welcome back, <strong>{firstName}</strong></p>
      </header>

      <div className="dashboard-section-heading">
        <div><span>AT A GLANCE</span><h2>Workspace overview</h2></div>
        <span className="dashboard-date">{new Intl.DateTimeFormat(undefined, { dateStyle: "full" }).format(new Date())}</span>
      </div>

      <div className="dashboard-stats">
        {summaryItems.map(({ key, label, detail, Icon, to, accent }) => (
          <Link className={`dashboard-stat dashboard-stat--${accent}`} to={to} key={key}>
            <span className="dashboard-stat__icon"><Icon /></span>
            <span className="dashboard-stat__label">{label}</span>
            <strong>
              {snapshot[key] === null ? "…" : snapshot[key] === false ? "—" : snapshot[key].length}
            </strong>
            <span className="dashboard-stat__detail">{detail}<ArrowOutwardRoundedIcon /></span>
          </Link>
        ))}
        <Link className="dashboard-stat dashboard-stat--amber" to="/reports">
          <span className="dashboard-stat__icon"><AssessmentRoundedIcon /></span>
          <span className="dashboard-stat__label">Reports ready</span>
          <strong>Explore</strong>
          <span className="dashboard-stat__detail">Generate secure summaries<ArrowOutwardRoundedIcon /></span>
        </Link>
      </div>

      {errors.length > 0 && (
        <div className="dashboard-warning" role="status">
          <span>Some workspace data could not be loaded: {errors.join(", ")}.</span>
          <span>Check your permissions or backend connection.</span>
        </div>
      )}

      <div className="dashboard-lower-grid">
        <section className="dashboard-panel">
          <div className="dashboard-panel__heading">
            <div><span>THE LATEST</span><h2>Recent cases</h2></div>
            <Link to="/cases">All cases <ArrowOutwardRoundedIcon /></Link>
          </div>
          {snapshot.cases === null ? (
            <p className="dashboard-inline-empty">Loading case activity…</p>
          ) : snapshot.cases === false ? (
            <p className="dashboard-inline-empty">Case records are unavailable. Check your access and retry.</p>
          ) : snapshot.cases.length ? (
            <div className="dashboard-case-list">
              {snapshot.cases.slice(0, 4).map((item) => (
                <div className="dashboard-case-row" key={item.id}>
                  <span className="dashboard-case-row__mark"><FolderOpenRoundedIcon /></span>
                  <span className="dashboard-case-row__copy">
                    <strong>{item.title}</strong>
                    <small>{item.case_number} <i /> {item.case_type || "Investigation"}</small>
                  </span>
                  <span className="dashboard-case-row__meta">
                    <b>{item.status || "Open"}</b>
                    <small>{readableDate(item.date_opened)}</small>
                  </span>
                </div>
              ))}
            </div>
          ) : (
            <div className="dashboard-inline-empty">No case records are available yet.</div>
          )}
        </section>

        <section className="dashboard-panel dashboard-panel--activity">
          <div className="dashboard-panel__heading">
            <div><span>ACCOUNTABILITY</span><h2>Recent activity</h2></div>
            <Link to="/audit">Audit trail <ArrowOutwardRoundedIcon /></Link>
          </div>
          {snapshot.audit === null ? (
            <p className="dashboard-inline-empty">Loading activity…</p>
          ) : snapshot.audit === false ? (
            <p className="dashboard-inline-empty">Activity is unavailable. Check your access and retry.</p>
          ) : recentActivity.length ? (
            <div className="dashboard-activity-list">
              {recentActivity.map((item, index) => (
                <div className="dashboard-activity-row" key={item.id || index}>
                  <span className={`dashboard-activity-row__icon dashboard-activity-row__icon--${index % 3}`}>
                    <HistoryRoundedIcon />
                  </span>
                  <span><strong>{item.description || item.action}</strong><small>{item.username || "DEMS user"} · {item.module || "Workspace"}</small></span>
                  <time>{readableDate(item.created_at)}</time>
                </div>
              ))}
            </div>
          ) : (
            <div className="dashboard-inline-empty">No activity has been recorded yet.</div>
          )}
        </section>
      </div>
    </section>
  );
}
