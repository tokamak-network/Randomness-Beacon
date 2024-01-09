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
                    <title>TON Random Airdrop</title>
                    <meta name="description" content="RandomAirdrop using Commit-Recover" />
                    <link rel="icon" href="../tokamaklogo.png" />
                </Head>
                <Header />
                <Component {...pageProps} />
            </NotificationProvider>
        </MoralisProvider>
    )
}

export default MyApp
// initializeonMount : is the optionality to hook into a server to add some more features to our website.
