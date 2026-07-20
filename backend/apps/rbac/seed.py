"""
Digital Evidence Management System (DEMS)

Module:
    RBAC

File:
    seed.py

Purpose:
    Default roles and permissions.
"""

DEFAULT_ROLES = [

    (
        "Administrator",
        "System administrator with full access.",
    ),

    (
        "Investigator",
        "Responsible for investigations and evidence collection.",
    ),

    (
        "Examiner",
        "Responsible for forensic examination.",
    ),

    (
        "Auditor",
        "Responsible for compliance and auditing.",
    ),

]


DEFAULT_PERMISSIONS = [
    # --------------------------
# Storage
# --------------------------

("storage.view", "View Stored Files"),
("storage.upload", "Upload Stored Files"),
("storage.verify", "Verify Stored Files"),

    # --------------------------
    # Cases
    # --------------------------

    ("cases.view", "View Cases"),
("cases.create", "Create Cases"),
("cases.update", "Update Cases"),
("cases.delete", "Delete Cases"),
("cases.assign", "Assign Cases"),
("cases.close", "Close Cases"),
("cases.archive", "Archive Cases"),

    # --------------------------
    # Evidence
    # --------------------------

    ("evidence.view", "View Evidence"),
    ("evidence.upload", "Upload Evidence"),
    ("evidence.update", "Update Evidence"),
    ("evidence.verify", "Verify Evidence"),
    ("evidence.download", "Download Evidence"),
    ("evidence.delete", "Delete Evidence"),

    # --------------------------
    # Custody
    # --------------------------

    ("custody.view", "View Chain of Custody"),
("custody.create", "Create Chain of Custody"),
("custody.update", "Update Chain of Custody"),
("custody.delete", "Delete Chain of Custody"),
("custody.transfer", "Transfer Evidence"),
("custody.receive", "Receive Evidence"),
("custody.verify", "Verify Chain of Custody"),
    # --------------------------
    # Audit
    # --------------------------

    ("audit.view", "View Audit Logs"),
("audit.delete", "Delete Audit Logs"),
("audit.export", "Export Audit Logs"),

    # --------------------------
    # Reports
    # --------------------------

    ("reports.generate", "Generate Reports"),

    # --------------------------
    # Dashboard
    # --------------------------

    ("dashboard.view", "View Dashboard"),

    # --------------------------
    # RBAC
    # --------------------------

    ("rbac.manage", "Manage Roles"),

    ("reports.view_report", "View Reports"),
    ("reports.generate_report", "Generate Reports"),
    ("reports.delete_report", "Delete Reports"),
]
DEFAULT_ROLE_PERMISSIONS = {

    "Administrator": [
        "*",
    ],

    "Investigator": [
        "cases.view",
        "cases.create",
        "cases.update",
        "cases.assign",
        "cases.close",

        "evidence.view",
        "evidence.upload",
        "evidence.download",

        "custody.view",
        "custody.transfer",

        "dashboard.view",
    ],

    "Examiner": [
        "cases.view",

        "evidence.view",
        "evidence.verify",
        "evidence.download",

        "custody.view",

        "reports.generate",

        "dashboard.view",
    ],

    "Auditor": [
        "audit.view",

        "custody.view",

        "reports.generate",

        "dashboard.view",
    ],
}