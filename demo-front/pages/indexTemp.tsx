import Round from "../components/Round"
import { useMoralis } from "react-moralis"
import { useState, useEffect } from "react"
import { useWeb3Contract } from "react-moralis"
import { abi, contractAddresses as contractAddressesJSON } from "../constants"
import { useInterval } from "use-interval"
import { useNotification, Bell } from "web3uikit"
import RankOfEachParticipants from "../components/RankOfEachParticipants"
import { BigNumber, BigNumberish, ethers } from "ethers"
import { SettedUpValues } from "../typechain-types/RandomAirdrop"
import { ICommitRevealRecoverRNG } from "../typechain-types/RandomAirdrop"
import Header from "../components/Header"
import { decodeError } from "ethers-decode-error"

export default function Home() {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const contractAddresses: { [key: string]: string[] } = contractAddressesJSON
    const randomAirdropAddress =
        chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null
    let [round, setRound] = useState<string>("")
    const [settedUpValues, setSettedUpValues] = useState<SettedUpValues>({
        T: "",
        n: "",
        nl: "",
        g: "",
        gl: "",
        h: "",
        hl: "",
        commitDuration: "",
        commitRevealDuration: "",
        setUpTime: "",
    })
    const [timeRemaining, setTimeRemaining] = useState<string>("")
    const [participatedRoundsLength, setParticipatedRoundsLength] = useState<string>("")
    const [participatedRounds, setParticipatedRounds] = useState<string[]>([])
    const [nextRound, setNextRound] = useState<string>("")
    const dispatch = useNotification()
    function str_pad_left(string: number, pad: string, length: number) {
        return (new Array(length + 1).join(pad) + string).slice(-length)
    }

    // @ts-ignore
    const { runContractFunction: registerNextRound } = useWeb3Contract()
    const [isFetching, setIsFetching] = useState(false)
    // @ts-ignore
    const { runContractFunction: getParticipantsLengthAtRound } = useWeb3Contract()
    const { runContractFunction: getNextRound } = useWeb3Contract({
        abi: abi,
        contractAddress: randomAirdropAddress!, //,
        functionName: "getNextRound", //,
        params: {},
    })
    async function getRankPointOfEachParticipantsFunction() {
        setIsFetching(true)
        const registerNextRoundOptions = {
            abi: abi,
            contractAddress: randomAirdropAddress!,
            functionName: "registerNextRound",
            params: {},
        }
        const provider = new ethers.providers.Web3Provider((window as any).ethereum, "any")
        // Prompt user for account connections
        await provider.send("eth_requestAccounts", [])
        const signer = provider.getSigner()
        const randomAirdropContract = new ethers.Contract(randomAirdropAddress!, abi, provider)
        try {
            const tx = await randomAirdropContract
                .connect(signer)
                .registerNextRound({ gasLimit: 120000 })
            await handleSuccess(tx)
        } catch (error: any) {
            console.log(error.message)
            const decodedError = decodeError(decodeError(error))
            dispatch({
                type: "error",
                message: decodedError.error,
                title: "Error Message",
                position: "topR",
                icon: <Bell />,
            })
            setIsFetching(false)
        }
    }
    const handleSuccess = async function (tx: any) {
        await tx.wait(1)
        setIsFetching(false)
        handleNewNotification()
    }
    const handleNewNotification = function () {
        dispatch({
            type: "info",
            message: "Transaction Completed",
            title: "Tx Notification",
            position: "topR",
            icon: <Bell />, //"bell",
        })
    }
    useInterval(() => {
        let commitDurationInt
        if (settedUpValues.commitDuration) {
            commitDurationInt = parseInt(settedUpValues.commitDuration.toString())
            if (commitDurationInt > 0) {
                let _timeRemaing =
                    commitDurationInt -
                    (Math.floor(Date.now() / 1000) - parseInt(settedUpValues.setUpTime.toString()))
                const minutes = Math.floor(_timeRemaing / 60)
                const seconds = _timeRemaing - minutes * 60
                if (_timeRemaing > -1)
                    setTimeRemaining(
                        str_pad_left(minutes, "0", 2) + ":" + str_pad_left(seconds, "0", 2)
                    )
            }
        }
    }, 1000)
    useEffect(() => {
        if (isWeb3Enabled) {
            updateUI()
        }
    }, [isWeb3Enabled, round])
    useInterval(() => {
        updateUI()
    }, 12000)
    // @ts-ignore
    const { runContractFunction: getSetUpValuesAtRound } = useWeb3Contract()
    const { runContractFunction: randomAirdropRound } = useWeb3Contract({
        abi: abi,
        contractAddress: randomAirdropAddress!, //,
        functionName: "randomAirdropRound", //,
        params: {},
    })
    const { runContractFunction: getParticipatedRounds } = useWeb3Contract({
        abi: abi,
        contractAddress: randomAirdropAddress!, //,
        functionName: "getParticipatedRounds", //,
        params: {},
    })

    async function updateUI() {
        let roundFromCall = (await randomAirdropRound({
            onError: (error) => console.log(error),
        })) as BigNumberish
        let nextRoundFromCall = (await getNextRound({
            onError: (error) => console.log(error),
        })) as BigNumberish
        setNextRound(nextRoundFromCall?.toString())
        if (roundFromCall === undefined) roundFromCall = 0
        setRound(roundFromCall.toString())
        const participantsLengthfromCallOptions = {
            abi: abi,
            contractAddress: randomAirdropAddress!,
            functionName: "getParticipantsLengthAtRound",
            params: { _round: nextRoundFromCall },
        }
        const participantsLengthfromCall = (await getParticipantsLengthAtRound({
            params: participantsLengthfromCallOptions,
            onError: (error) => console.log(error),
        })) as BigNumberish
        setParticipatedRoundsLength(participantsLengthfromCall?.toString())
        const participatedRoundsfromCall = (await getParticipatedRounds({
            onError: (error) => console.log(error),
        })) as BigNumber[]
        let temp = []

        if (participatedRoundsfromCall) {
            for (let i = 0; i < participatedRoundsfromCall.length; i++) {
                temp.push(participatedRoundsfromCall[i].toString())
            }
            setParticipatedRounds(temp)
        }
        await getGetSetUpValuesAtRound(roundFromCall)
    }
    async function getGetSetUpValuesAtRound(roundFromCall: BigNumberish) {
        const setUpValuesAtRoundOptions = {
            abi: abi,
            contractAddress: randomAirdropAddress!,
            functionName: "getSetUpValuesAtRound",
            params: { _round: roundFromCall },
        }
        const result: ICommitRevealRecoverRNG.SetUpValueAtRoundStructOutput =
            (await getSetUpValuesAtRound({
                params: setUpValuesAtRoundOptions,
                onError: (error) => console.log(error),
            })) as ICommitRevealRecoverRNG.SetUpValueAtRoundStructOutput
        if (result === undefined) return
        setSettedUpValues({
            T: result["T"].toString(),
            n: result["n"]["val"].toString(),
            nl: result["n"]["bitlen"].toString(),
            g: result["g"]["val"].toString(),
            gl: result["g"]["bitlen"].toString(),
            h: result["h"]["val"].toString(),
            hl: result["h"]["bitlen"].toString(),
            commitDuration: result["commitDuration"].toString(),
            commitRevealDuration: result["commitRevealDuration"].toString(),
            setUpTime: result["setUpTime"].toString(),
        })
    }
    return (
        <>
            <Header />
            <div className="bg-slate-50	opacity-80 min-h-screen bg-repeat-y bg-cover bg-center py-10">
                <div
                    style={{ minWidth: "852px" }}
                    className="bg-white	container mx-auto w-6/12 rounded-3xl border-dashed border-slate-300 border-2"
                >
                    <Round round={round} />
                    {randomAirdropAddress ? (
                        <div>
                            <div className="p-5">
                                <div className="border-dashed border-slate-300 border-2 rounded-lg p-10">
                                    <div className="mb-2 font-bold">
                                        Register For Round{" "}
                                        <span className="font-black">{nextRound}</span>
                                    </div>
                                    <button
                                        id="enterEventByCommit"
                                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded ml-auto mt-7"
                                        disabled={isFetching}
                                        type="button"
                                        onClick={getRankPointOfEachParticipantsFunction}
                                    >
                                        {isFetching ? (
                                            <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                                        ) : (
                                            <div>Register</div>
                                        )}
                                    </button>
                                    <div className="pt-2">
                                        Number of participants registered :
                                        <span className="font-bold">
                                            {" "}
                                            {participatedRoundsLength}
                                        </span>
                                    </div>
                                </div>
                            </div>
                            <div>
                                <RankOfEachParticipants
                                    round={round}
                                    participatedRounds={participatedRounds}
                                />
                            </div>
                        </div>
                    ) : (
                        <div></div>
                    )}
                </div>
            </div>
        </>
    )
}
