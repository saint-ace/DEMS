import {
    AppBar,
    Toolbar,
    Typography,
    IconButton,
    Avatar,
    Box,
} from "@mui/material";

import NotificationsIcon from "@mui/icons-material/Notifications";

const drawerWidth = 250;

export default function Topbar() {
    return (
        <AppBar
            position="fixed"
            sx={{
                width: `calc(100% - ${drawerWidth}px)`,
                ml: `${drawerWidth}px`,
            }}
        >
            <Toolbar>

                <Typography
                    variant="h6"
                    sx={{ flexGrow: 1 }}
                >
                    Digital Evidence Management System
                </Typography>

                <IconButton color="inherit">
                    <NotificationsIcon />
                </IconButton>

                <Box ml={2}>
                    <Avatar>S</Avatar>
                </Box>

            </Toolbar>
        </AppBar>
    );
}