import React from 'react';
import Link from 'next/link';
import { CareerDayLogo, CoverLogo } from './Logos';
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
                    <Link href="/frontend/public" className="text-white">Home</Link>
                </li>
                <li>
                    <Link href="/schedule" className="text-white">My Schedule</Link>
                </li>
                <li>
                    <Link href="/practical" className="text-white">Practical Information</Link>
                </li>
            </ul>
        </nav>
    );
};

export default Navbar;