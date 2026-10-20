import { Box, Typography } from "@mui/material";

export default function PageContainer({
    title,
    children,
}) {
    return (
        <Box p={3}>
            <Typography
                variant="h4"
                gutterBottom
            >
                {title}
            </Typography>

            {children}
        </Box>
    );
}