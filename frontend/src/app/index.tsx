import React from 'react';
import App from './components/App';
import {GetServerSideProps} from "next";
import axios from 'axios'

const Home: React.FC = () => {
    return <App />;
};

export default Home;