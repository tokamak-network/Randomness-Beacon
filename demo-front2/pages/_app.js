import { MoralisProvider } from "react-moralis"
import { NotificationProvider } from "web3uikit"
import "../styles/globals.css"
import Head from "next/head"
import Round from "../components/Round"
import Header from "../components/Header"

function MyApp({ Component, pageProps }) {
    return (
        <MoralisProvider initializeOnMount={false}>
            <NotificationProvider>
                <Head>
                    <title>Commit-Rover Raffle</title>
                    <meta name="description" content="Raffle using Commit-Recover" />
                    <link rel="icon" href="/favicon.ico" />
                </Head>
                <Header />
                <Component {...pageProps} />
            </NotificationProvider>
        </MoralisProvider>
    )
}

export default MyApp
// initializeonMount : is the optionality to hook into a server to add some more features to our website.
