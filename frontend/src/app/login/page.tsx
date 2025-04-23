'use client'
import { useEffect } from 'react'

const LoginPage = () => {
    useEffect(() => {
        window.location.href = 'http://localhost:8000/login?referrer=/'
    }, [])

    return <p>Redirecting to Cover login...</p>
}

export default LoginPage
