import {
    Drawer,
    Toolbar,
    List,
    ListItemButton,
    ListItemIcon,
    ListItemText,
} from "@mui/material";

import { NavLink } from "react-router-dom";

import menuItems from "./menuItems";

const drawerWidth = 250;

export default function Sidebar() {
    return (
        <Drawer
            variant="permanent"
            sx={{
                width: drawerWidth,
                flexShrink: 0,
                "& .MuiDrawer-paper": {
                    width: drawerWidth,
                    boxSizing: "border-box",
                },
            }}
        >
            <Toolbar />

            <List>
                {menuItems.map((item) => (
                    <ListItemButton
                        key={item.text}
                        component={NavLink}
                        to={item.path}
                        sx={{
                            "&.active": {
                                bgcolor: "primary.main",
                                color: "white",

                                "& .MuiListItemIcon-root": {
                                    color: "white",
                                },
                            },
                        }}
                    >
                        <ListItemIcon>
                            {item.icon}
                        </ListItemIcon>

                        <ListItemText
                            primary={item.text}
                        />
                    </ListItemButton>
                ))}
            </List>
        </Drawer>
    );
}