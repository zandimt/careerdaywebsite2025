import type { AppProps } from "next/app";
import Head from "next/head";
import "../styles/globals.css"; // Import global styles

export default function MyApp({ Component, pageProps }: AppProps) {
    return (
        <>
            <Head>
                <title>Cover Career Day</title>
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
                <link rel="icon" href="/logos/favicon.ico"/>
            </Head>
            <Component {...pageProps} />
        </>
    );
}
