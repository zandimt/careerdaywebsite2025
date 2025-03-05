// components/Footer.jsx
import React from 'react';
import { CoverLogo } from '../components/logos';

function Footer() {
    return (
        <footer style={footerStyle}>
            <div style={containerStyle}>
                {/* Cover Section */}
                <div style={sectionStyle}>
                    <a href="https://svcover.nl" target="_blank" rel="noopener noreferrer" style={logoLinkStyle}>
                        <CoverLogo/>
                    </a>
                    <p style={textStyle} >
                        Study Association for Artificial Intelligence, Computing
                        Science, and Computational Cognitive Science.
                    </p>
                </div>

                {/* Legal Section */}
                <div style={sectionStyle}>
                    <h3 style={headingStyle}>Resources</h3>
                    <ul style={listStyle}>
                        <li>
                            <a href="https://svcover.nl/committees/comexa" style={linkStyle}>
                                Committee of External Affairs
                            </a>
                        </li>
                        <li>
                            <a href="https://svcover.nl/sponsoring" style={linkStyle}>
                                Information for Companies
                            </a>
                        </li>
                        <li>
                            <a href="https://sd.svcover.nl/Privacy%20Statement/Privacy%20statement.pdf" style={linkStyle}>
                                Privacy Statement
                            </a>
                        </li>
                        <li>
                            <a href="https://www.svcover.nl/cancellation-policy" style={linkStyle}>
                                Cancellation Policy
                            </a>
                        </li>
                    </ul>
                </div>

                {/* Contact Section */}
                <div style={sectionStyle}>
                    <h3 style={headingStyle}>Contact</h3>
                    <ul style={listStyle}>
                        <li>
                            <a href="mailto:comexa@svcover.nl" style={linkStyle}>
                                comexa@svcover.nl
                            </a>
                        </li>
                        <li>
                            <a href="mailto:board@svcover.nl" style={linkStyle}>
                                board@svcover.nl
                            </a>
                        </li>
                        <li>Study Association Cover</li>
                        <li>Postbus 407</li>
                        <li>9700 AK Groningen</li>
                        <li>The Netherlands</li>
                    </ul>
                </div>
            </div>

            {/* Copyright Notice */}
            <div style={copyrightStyle}>
                <p style={textStyle}>
                    © 2025. All rights reserved.
                </p>
            </div>
        </footer>
    );
}

// Styles
const footerStyle = {
    backgroundColor: '#1a1a1a',
    color: '#ffffff',
    padding: '20px',
    marginTop: 'auto', // Ensures footer sticks to the bottom if the page is short
    width: '100vw',
    position: 'relative',
    bottom: '0',
    overflowY: 'auto',
};

const containerStyle = {
    maxWidth: '100%',
    display: 'flex',
    justifyContent: 'space-between',
    flexWrap: 'wrap',
    gap: '20px',
    paddingLeft: '10vw',
};

const sectionStyle = {
    flex: '1',
    minWidth: '200px',
    marginBottom: '20px',
};

const headingStyle = {
    fontSize: '1.25rem',
    marginBottom: '10px',
};

const textStyle = {
    fontSize: '0.9rem',
    lineHeight: '1.5',
    width: '80%',
};

const listStyle = {
    listStyle: 'none',
    padding: '0',
    margin: '0',
};

const linkStyle = {
    color: '#ffffff',
    textDecoration: 'none',
    transition: 'color 0.3s ease',
};

linkStyle[':hover'] = {
    color: '#cccccc',
};

const copyrightStyle = {
    display: 'flex',
    justifyContent: 'center',
    textAlign: 'center',
    marginTop: '20px',
    borderTop: '1px solid #333',
    paddingTop: '10px',
};

const logoLinkStyle = {
    display: 'inline-block',
    textDecoration: 'none',
};

export default Footer;