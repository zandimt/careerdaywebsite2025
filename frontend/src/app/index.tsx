import React from 'react';
import App from './components/App';
import {GetServerSideProps} from "next";
import axios from 'axios'

const COVER_LOGIN_URL = 'https://svcover.nl/login?referrer=https://careerday.svcover.nl'

export const getServerSideProps: GetServerSideProps = async (context) => {
    const { req } = context
    const cookie = req.headers.cookie || ''

    try {
        const response = await axios.get('localhost:8001/api/check-auth/', {
            headers: {
                Cookie: cookie,
            },
            withCredentials: true,
        })

        if (response.data.authenticated) {
            return {
                redirect: {
                    destination: '/dashboard',
                    permanent: false,
                },
            }
        }
    } catch (err) {
        return {
            redirect: {
                destination: COVER_LOGIN_URL,
                permanent: false,
            },
        }
    }

    // Fallback — shouldn't be hit, but just in case
    return {
        redirect: {
            destination: COVER_LOGIN_URL,
            permanent: false,
        },
    }
}

const Home: React.FC = () => {
    return <App />;
};

export default Home;