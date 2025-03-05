import React from 'react';
import { CoverLogo } from '../logos';
import './footer.css';

function Footer() {
    return (
        <footer className="footer">
            <div className="container">
                {/* Cover Section */}
                <div className="section">
                    <a href="https://svcover.nl" target="_blank" rel="noopener noreferrer" className="logo-link">
                        <CoverLogo/>
                    </a>
                    <p className="text">
                        Study Association for Artificial Intelligence, Computing
                        Science, and Computational Cognitive Science.
                    </p>
                </div>

                {/* Legal Section */}
                <div className="section">
                    <h3 className="heading">Information</h3>
                    <ul className="list">
                        <li>
                            <a href="https://svcover.nl/committees/comexa" className="link">
                                Committee of External Affairs
                            </a>
                        </li>
                        <li>
                            <a href="https://svcover.nl/sponsoring" className="link">
                                Information for Companies
                            </a>
                        </li>
                        <br/>
                        <li>
                            <a href="https://sd.svcover.nl/Privacy%20Statement/Privacy%20statement.pdf" className="link">
                                Privacy Statement
                            </a>
                        </li>
                        <li>
                            <a href="https://www.svcover.nl/cancellation-policy" className="link">
                                Cancellation Policy
                            </a>
                        </li>
                    </ul>
                </div>

                {/* Contact Section */}
                <div className="section">
                    <h3 className="heading">Contact</h3>
                    <ul className="list">
                        <li>
                            <a href="mailto:comexa@svcover.nl" className="link">
                                comexa@svcover.nl
                            </a>
                        </li>
                        <li>
                            <a href="mailto:board@svcover.nl" className="link">
                                board@svcover.nl
                            </a>
                        </li>
                        <br/>
                        <li>Studievereniging Cover</li>
                        <li>Postbus 407</li>
                        <li>9700 AK Groningen</li>
                        <li>The Netherlands</li>
                    </ul>
                </div>
            </div>

            {/* Copyright Notice */}
            <div className="copyright">
                <p className="text">
                    Created by{' '}
                    <a href="https://www.svcover.nl/profile/3274" className="link">
                        Andi Toader
                    </a>
                    {' '}and{' '}
                    <a href="https://www.svcover.nl/profile/3400" className="link">
                        Marcus Harald Olof Persson
                    </a>.
                </p>
            </div>
        </footer>
    );
}

export default Footer;