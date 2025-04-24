// next.config.ts
import type { NextConfig } from 'next'
import { PHASE_DEVELOPMENT_SERVER } from 'next/constants'

const nextConfig: NextConfig = {
    reactStrictMode: true,
    env: {
        NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
    },
}

export default (phase: string) => {
    if (phase === PHASE_DEVELOPMENT_SERVER) {
        return nextConfig
    }

    return {
        ...nextConfig,
        // You can add production-specific config here if needed
    }
}

// next.config.js
module.exports = {
    async redirects() {
        return [
            {
                source: '/home',
                destination: '/', // or any default page
                permanent: true, // 308 permanent redirect
            },
        ];
    },
    async rewrites() {
        return [
            {
                source: '/api/svcover',
                destination: 'http://backend:8000/api/svcover/',
            },
            {
                source: '/api/settings',
                destination: 'http://backend:8000/api/settings/',
            },
            {
                source: '/api/participants/:path*',
                destination: 'http://backend:8000/api/participants/:path*',
            },
            {
                source: '/api/organisations',
                destination: 'http://backend:8000/api/organisations/',
            },
            {
                source: '/api/organisations/:organisation_id',
                destination: 'http://backend:8000/api/organisations/:organisation_id/',
            },
            {
                source: '/uploads/:path*',
                destination: 'http://backend:8000/uploads/:path*',
            },
            {
                source: '/api/timeslots',
                destination: 'http://backend:8000/api/timeslots/',
            },
            {
                source: '/api/timeslots/:time_slot_id',
                destination: 'http://backend:8000/api/timeslots/:time_slot_id/',
            },
            {
                source: '/api/sessions',
                destination: 'http://backend:8000/api/sessions/',
            },
            {
                source: '/api/sessions/:session_id',
                destination: 'http://backend:8000/api/sessions/:session_id/',
            }
        ];
    }
};
