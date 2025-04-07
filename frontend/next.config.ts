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
