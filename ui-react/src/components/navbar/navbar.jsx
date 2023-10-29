import React, { useState } from 'react';
import {
    AppBar,
    Toolbar,
    IconButton,
    Drawer,
    List,
    ListItem,
    ListItemIcon,
    ListItemText,
    Typography
} from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import { Link } from 'react-router-dom';
import Paperlinks from '../../assets/paperlinks_logo_white_all.png';
import './navbar.css';

const Navbar = () => {
    const [drawerOpen, setDrawerOpen] = useState(false);

    const handleDrawerOpen = () => {
        setDrawerOpen(true);
    };

    const handleDrawerClose = () => {
        setDrawerOpen(false);
    };

    const menuItems = [
        { icon: <AccountCircleIcon />, text: 'Home', link: '/' },
        { icon: <AccountCircleIcon />, text: 'Insights', link: '/insights' },
        { icon: <AccountCircleIcon />, text: 'Data', link: '/data' },
        { icon: <AccountCircleIcon />, text: 'Prediction', link: '/prediction' },
        // Add more menu items as needed
    ];

    return (
        <AppBar position="static">
            <Toolbar className="navbar-toolbar">
                {/* Hamburger menu icon */}
                <IconButton color="inherit" onClick={handleDrawerOpen}>
                    <MenuIcon />
                </IconButton>

                {/* Logo on the far left */}
                <IconButton color="inherit" component={Link} to="/">
                    <img src={Paperlinks} height={"25px"} alt="Logo" />
                </IconButton>


                {/* Account icon on the far right */}
                <IconButton color="inherit" component={Link} to="/login">
                    <AccountCircleIcon />
                </IconButton>

                {/* Drawer for side menu */}
                <Drawer anchor="left" open={drawerOpen} onClose={handleDrawerClose}>
                    <List>
                        {menuItems.map((item, index) => (
                            <ListItem button key={item.text} component={Link} to={item.link} onClick={handleDrawerClose}>
                                <ListItemIcon>{item.icon}</ListItemIcon>
                                <ListItemText primary={item.text} />
                            </ListItem>
                        ))}
                    </List>
                </Drawer>
            </Toolbar>
        </AppBar>
    );
};

export default Navbar;
