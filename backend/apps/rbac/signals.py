DEFAULT_ROLE_PERMISSIONS = {

    "Administrator": [
        "*",
    ],

    "Investigator": [
        "cases.view",
        "cases.create",
        "cases.update",

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