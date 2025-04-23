import { useEffect } from 'react'

const LoginPage = () => {
    useEffect(() => {
        window.location.href = 'https://svcover.nl/login?referrer=https://careerday.svcover.nl'
    }, [])

    return <p>Redirecting to Cover login...</p>
}

export default LoginPage
