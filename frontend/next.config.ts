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
                source: '/api/organisations/:path*',
                destination: 'http://backend:8000/api/organisations/:path*',
            },
        ];
    }
};
