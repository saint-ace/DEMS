import DashboardIcon from "@mui/icons-material/Dashboard";
import FolderIcon from "@mui/icons-material/Folder";
import DescriptionIcon from "@mui/icons-material/Description";
import LinkIcon from "@mui/icons-material/Link";
import AssessmentIcon from "@mui/icons-material/Assessment";
import HistoryIcon from "@mui/icons-material/History";
import PeopleIcon from "@mui/icons-material/People";
import SecurityIcon from "@mui/icons-material/Security";
import SettingsIcon from "@mui/icons-material/Settings";

const menuItems = [
    {
        text: "Dashboard",
        icon: <DashboardIcon />,
        path: "/",
    },
    {
        text: "Cases",
        icon: <FolderIcon />,
        path: "/cases",
    },
    {
        text: "Evidence",
        icon: <DescriptionIcon />,
        path: "/evidence",
    },
    {
        text: "Chain of Custody",
        icon: <LinkIcon />,
        path: "/custody",
    },
    {
        text: "Reports",
        icon: <AssessmentIcon />,
        path: "/reports",
    },
    {
        text: "Audit Logs",
        icon: <HistoryIcon />,
        path: "/audit",
    },
    {
        text: "Users",
        icon: <PeopleIcon />,
        path: "/users",
    },
    {
        text: "Roles",
        icon: <SecurityIcon />,
        path: "/roles",
    },
    {
        text: "Settings",
        icon: <SettingsIcon />,
        path: "/settings",
    },
];

export default menuItems;