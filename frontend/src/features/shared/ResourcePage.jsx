import { useCallback, useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import RefreshRoundedIcon from "@mui/icons-material/RefreshRounded";
import SearchRoundedIcon from "@mui/icons-material/SearchRounded";

function formatValue(value) {
  if (value === null || value === undefined || value === "") return "—";
  if (typeof value === "boolean") return value ? "Yes" : "No";
  if (typeof value === "object") return value.name || value.label || "—";

  if (typeof value === "string" && /^\d{4}-\d{2}-\d{2}/.test(value)) {
    const date = new Date(value);
    if (!Number.isNaN(date.getTime())) {
      return new Intl.DateTimeFormat(undefined, {
        dateStyle: "medium",
        ...(value.includes("T") ? { timeStyle: "short" } : {}),
      }).format(date);
    }
  }

  return String(value);
}

function statusClass(value) {
  const state = String(value || "").toLowerCase();
  if (/complete|closed|verified|active|received|analyzed/.test(state)) return "is-positive";
  if (/pending|generating|review|analysis/.test(state)) return "is-progress";
  if (/failed|disposed|inactive|denied/.test(state)) return "is-negative";
  return "is-neutral";
}

function describeRequestError(requestError) {
  const statusCode = requestError?.response?.status;
  if (statusCode === 401) {
    return "Your session has expired. Sign in again to load this workspace.";
  }
  if (statusCode === 403) {
    return "Your account does not have permission to view this section.";
  }
  return requestError?.response?.data?.detail ||
    requestError?.response?.data?.message ||
    requestError?.message ||
    "Could not load this section.";
}

export default function ResourcePage({ config }) {
  const [rows, setRows] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadRows = useCallback(async () => {
    setLoading(true);
    setError("");
    try {
      const result = await config.service.list();
      if (!Array.isArray(result)) {
        throw new Error("The API returned an unexpected response.");
      }
      setRows(result);
    } catch (requestError) {
      setError(describeRequestError(requestError));
    } finally {
      setLoading(false);
    }
  }, [config.service]);

  useEffect(() => {
    let active = true;
    config.service.list()
      .then((result) => {
        if (!active) return;
        if (!Array.isArray(result)) {
          throw new Error("The API returned an unexpected response.");
        }
        setRows(result);
      })
      .catch((requestError) => {
        if (active) setError(describeRequestError(requestError));
      })
      .finally(() => {
        if (active) setLoading(false);
      });
    return () => { active = false; };
  }, [config.service]);

  const filteredRows = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase();
    if (!normalizedQuery) return rows;
    return rows.filter((row) =>
      config.columns.some(({ key, value }) => {
        const field = value ? value(row) : row[key];
        return String(field ?? "").toLowerCase().includes(normalizedQuery);
      })
    );
  }, [config.columns, query, rows]);

  const Icon = config.icon;

  return (
    <section className="resource-page">
      <header className="workspace-hero">
        <div className="workspace-hero__copy">
          <div className="workspace-eyebrow">
            <span className="workspace-eyebrow__dot" />
            DEMS WORKSPACE
          </div>
          <h1>{config.title}</h1>
          <p>{config.description}</p>
        </div>
        <div className="workspace-hero__art" aria-hidden="true">
          <span className="workspace-hero__ring workspace-hero__ring--outer" />
          <span className="workspace-hero__ring workspace-hero__ring--inner" />
          <span className="workspace-hero__icon"><Icon /></span>
          <span className="workspace-hero__spark workspace-hero__spark--one" />
          <span className="workspace-hero__spark workspace-hero__spark--two" />
        </div>
      </header>

      <div className="resource-toolbar">
        <div className="resource-toolbar__heading">
          <div className="resource-icon"><Icon /></div>
          <div>
            <h2>{config.sectionTitle || `${config.title} register`}</h2>
            <p>Records are loaded securely from the DEMS API.</p>
          </div>
        </div>
        <div className="resource-toolbar__actions">
          <label className="resource-search">
            <SearchRoundedIcon aria-hidden="true" />
            <input
              type="search"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder={`Search ${config.title.toLowerCase()}...`}
              aria-label={`Search ${config.title}`}
            />
          </label>
          <button
            className="icon-button"
            type="button"
            onClick={loadRows}
            disabled={loading}
            aria-label="Refresh records"
            title="Refresh"
          >
            <RefreshRoundedIcon />
          </button>
          {config.action && (
            <Link className="primary-action" to={config.action.to}>
              {config.action.label}
            </Link>
          )}
        </div>
      </div>

      <div className="resource-summary">
        <div className="summary-card">
          <span className="summary-card__label">Total records</span>
          <strong>{loading ? "…" : rows.length}</strong>
          <span className="summary-card__hint">Across your workspace</span>
        </div>
        <div className="summary-card summary-card--accent">
          <span className="summary-card__label">Showing</span>
          <strong>{loading ? "…" : filteredRows.length}</strong>
          <span className="summary-card__hint">
            {query ? "Matching your search" : "Current results"}
          </span>
        </div>
        <div className="summary-card summary-card--quiet">
          <span className="summary-card__label">Workspace status</span>
          <strong className="summary-live"><i /> Live</strong>
          <span className="summary-card__hint">Connected to backend</span>
        </div>
      </div>

      {error ? (
        <div className="resource-error" role="alert">
          <span>{error}</span>
          <button type="button" onClick={loadRows}>Try again</button>
        </div>
      ) : (
        <div className="resource-table-card">
          <div className="resource-table-card__top">
            <div>
              <span className="resource-table-card__eyebrow">RECORDS</span>
              <h2>{config.tableTitle || config.title}</h2>
            </div>
            <span className="record-count">
              {loading ? "Syncing…" : `${filteredRows.length} records`}
            </span>
          </div>
          <div className="resource-table-scroll">
            <table className="resource-table">
              <thead>
                <tr>
                  {config.columns.map((column) => (
                    <th key={column.key}>{column.label}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {loading ? (
                  Array.from({ length: 4 }, (_, index) => (
                    <tr key={`loading-${index}`}>
                      {config.columns.map((column) => (
                        <td key={column.key}><span className="table-skeleton" /></td>
                      ))}
                    </tr>
                  ))
                ) : filteredRows.length ? (
                  filteredRows.map((row, index) => (
                    <tr key={row.id || row.uuid || index}>
                      {config.columns.map((column) => {
                        const value = column.value ? column.value(row) : row[column.key];
                        return (
                          <td key={column.key}>
                            {column.render ? column.render(value, row) :
                              column.status ? (
                                <span className={`status-pill ${statusClass(value)}`}>
                                  <i />{formatValue(value)}
                                </span>
                              ) : (
                                <span className={column.mono ? "cell-mono" : ""}>
                                  {formatValue(value)}
                                </span>
                              )}
                          </td>
                        );
                      })}
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={config.columns.length}>
                      <div className="table-empty">
                        <span className="table-empty__icon"><Icon /></span>
                        <strong>{query ? "No matching records" : `No ${config.title.toLowerCase()} yet`}</strong>
                        <span>
                          {query
                            ? "Try a different search phrase."
                            : "When records are added, they will appear here."}
                        </span>
                      </div>
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </section>
  );
}
