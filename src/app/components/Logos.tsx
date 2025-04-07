import React from 'react';
import Image from 'next/image';
import Link from 'next/link';

const CareerDayLogo: React.FC = () => {
    return (
        <div className="careerday-logo">
            <Link href="/">
                <div className="careerday-wrapper">
                    <Image src="/logos/careerday.svg" alt="Career Day" width={202} height={32} />
                    <Image src="/logos/careerday_wide.svg" alt="Career Day" className="hover-logo" width={202} height={32} />
                </div>
            </Link>
        </div>
    );
};

const CoverLogo: React.FC = () => {
    return (
        <div className="cover-logo">
            <Link href="https://svcover.nl/" target="_blank" rel="noopener noreferrer">
                <div className="cover-wrapper">
                    <Image src="/logos/cover.svg" alt="Cover" width={120} height={32}/>
                </div>
            </Link>
        </div>
    )
}


export { CareerDayLogo, CoverLogo };