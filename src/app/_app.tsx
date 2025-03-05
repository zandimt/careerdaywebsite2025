import type { AppProps } from "next/app";
import Head from "next/head";
import "../styles/globals.css"; // Import global styles

export default function MyApp({ Component, pageProps }: AppProps) {
    return (
        <>
            <Head>
                <title>My Next.js App</title>
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
                <link rel="icon" href="/favicon.ico"/>
            </Head>
            <Component {...pageProps} />
        </>
    );
}
