"use client";

import React from 'react';
import Link from 'next/link';
import { CareerDayLogo, CoverLogo } from './Logos';
import DashboardButton from "./DashboardButton";
import '../../styles/navbar.css';
import '../../styles/logos.css';


const Navbar: React.FC = () => {
    return (
        <nav className="navbar">
            <div className="logo-container">
                <CoverLogo />
                <CareerDayLogo />
            </div>
            <ul className="nav-links">
                <li>
                    <Link href="/home" className="text-white">Home</Link>
                </li>
                <li>
                    <Link href="/schedule" className="text-white">Schedule</Link>
                </li>
                <li>
                    <Link href="/practical" className="text-white">Practical Information</Link>
                </li>
                <DashboardButton />
            </ul>
        </nav>
);
};

export default Navbar;