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
                    <Link href="/home" className="text-white">Home</Link>
                </li>
                <li>
                    <Link href="/schedule" className="text-white">Schedule</Link>
                </li>
                <li>
                    <Link href="/practical" className="text-white">Practical Information</Link>
                </li>
                <li>
                    <Link href="/dashboard" className="text-white"><img width="32" height="32"
                                                                        src="https://img.icons8.com/windows/32/user.png"
                                                                        alt="user"/></Link>
                </li>
            </ul>
        </nav>
);
};

export default Navbar;