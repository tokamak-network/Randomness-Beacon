import { BigNumber, BigNumberish } from "ethers"
import { useEffect, useState } from "react"
import { useMoralis, useWeb3Contract } from "react-moralis"
import { useInterval } from "use-interval"
import { Widget } from "web3uikit"
import Commit from "../components/Commit"
import Header from "../components/Header"
import Round from "../components/Round"
import {
    airdropConsumerAbi,
    consumerContractAddress as consumerContractAddressJSON,
    coordinatorContractAddress as coordinatorContractAddressJSON,
    crrngAbi,
} from "../constants"
interface ValueAtRound {
    startTime: BigNumberish
    numOfPariticipants: BigNumberish
    count: BigNumberish
    consumer: string
    bStar: string
    commitsString: string
    omega: BigNumberish
    stage: BigNumberish
    isCompleted: boolean
    isAllRevealed: boolean
}

export default function Home() {
    const { chainId: chainIdHex, isWeb3Enabled, account } = useMoralis()
    const chainId = parseInt(chainIdHex!).toString()
    const consumerContractAddresses: { [key: string]: string[] } = consumerContractAddressJSON
    const coordinatorContractAddress: { [key: string]: string[] } = coordinatorContractAddressJSON
    const randomAirdropAddress =
        chainId in consumerContractAddresses
            ? consumerContractAddresses[chainId][consumerContractAddresses[chainId].length - 1]
            : null
    const coordinatorAddress =
        chainId in coordinatorContractAddress
            ? coordinatorContractAddress[chainId][coordinatorContractAddress[chainId].length - 1]
            : null
    let [round, setRound] = useState<string>("")
    // @ts-ignore
    const { runContractFunction: getValuesAtRound } = useWeb3Contract()
    const [valuesAtRound, setValuesAtRound] = useState<ValueAtRound>({
        startTime: BigNumber.from(0),
        numOfPariticipants: BigNumber.from(0),
        count: BigNumber.from(0),
        consumer: "",
        bStar: "",
        commitsString: "",
        omega: BigNumber.from(0),
        stage: BigNumber.from(0),
        isCompleted: false,
        isAllRevealed: false,
    })
    const [timeRemaining, setTimeRemaining] = useState<string>(
        str_pad_left(0, "0", 2) + ":" + str_pad_left(0, "0", 2)
    )
    const [started, setStarted] = useState("")
    const [participatedRounds, setParticipatedRounds] = useState<string[]>([])
    function str_pad_left(string: number, pad: string, length: number) {
        return (new Array(length + 1).join(pad) + string).slice(-length)
    }
    useInterval(() => {
        let commitDurationInt
        commitDurationInt = 120
        let _timeRemaing =
            commitDurationInt -
            (Math.floor(Date.now() / 1000) - parseInt(valuesAtRound.startTime.toString()))
        const minutes = Math.floor(_timeRemaing / 60)
        const seconds = _timeRemaing - minutes * 60
        if (_timeRemaing > -1)
            setTimeRemaining(str_pad_left(minutes, "0", 2) + ":" + str_pad_left(seconds, "0", 2))
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
    const { runContractFunction: getNextRandomAirdropRound } = useWeb3Contract({
        abi: airdropConsumerAbi,
        contractAddress: randomAirdropAddress!, //,
        functionName: "getNextRandomAirdropRound", //,
        params: {},
    })
    // @ts-ignore
    const { runContractFunction: getParticipatedRounds } = useWeb3Contract()

    async function updateUI() {
        let roundFromCall = (await getNextRandomAirdropRound({
            onError: (error) => console.log(error),
        })) as BigNumberish
        roundFromCall =
            parseInt(roundFromCall.toString()) == 0 ? 0 : parseInt(roundFromCall.toString()) - 1
        setRound(roundFromCall.toString())
        const valuesAtRoundFromCallOptions = {
            abi: crrngAbi,
            contractAddress: coordinatorAddress!,
            functionName: "getValuesAtRound",
            params: {
                _round: roundFromCall,
            },
        }
        const valuesAtRoundFromCall = (await getValuesAtRound({
            params: valuesAtRoundFromCallOptions,
            onError: (error) => console.log(error),
        })) as ValueAtRound
        setValuesAtRound(valuesAtRoundFromCall)
        const participatedRoundsfromCallOptions = {
            abi: airdropConsumerAbi,
            contractAddress: randomAirdropAddress!,
            functionName: "getParticipatedRounds",
            params: { participantAddress: account },
        }
        const participatedRoundsfromCall: BigNumber[] = (await getParticipatedRounds({
            params: participatedRoundsfromCallOptions,
            onError: (error) => console.log(error),
        })) as BigNumber[]
        let temp = []
        if (participatedRoundsfromCall) {
            for (let i = 0; i < participatedRoundsfromCall.length; i++) {
                temp.push(participatedRoundsfromCall[i].toString())
            }
            setParticipatedRounds(temp)
        }
        if (
            valuesAtRoundFromCall.startTime !== undefined &&
            valuesAtRoundFromCall.startTime != "0"
        ) {
            setStarted("Started!")
        } else {
            setStarted("Not Started")
        }
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
                            <div className="border-dashed border-slate-300 border-2 rounded-lg m-5 truncate hover:text-clip ">
                                <div className="mt-10 ml-10 font-bold">Current Round Info</div>
                                {valuesAtRound ? (
                                    <div
                                        style={{
                                            display: "grid",
                                            gap: "20px",
                                            padding: "40px 20px",
                                        }}
                                    >
                                        <section style={{ display: "flex", gap: "20px" }}>
                                            <Widget info={timeRemaining} title="TIME REMAINING" />

                                            <Widget
                                                info={
                                                    str_pad_left(Math.floor(120 / 60), "0", 2) +
                                                    " min, " +
                                                    str_pad_left(
                                                        120 - Math.floor(120 / 60) * 60,
                                                        "0",
                                                        2
                                                    ) +
                                                    " sec"
                                                }
                                                title="COMMIT DURATION"
                                            ></Widget>
                                            <Widget
                                                info={
                                                    valuesAtRound.startTime
                                                        ? new Date(
                                                              Number(valuesAtRound.startTime) *
                                                                  1000
                                                          )
                                                              .toLocaleString()
                                                              .slice(5)
                                                        : "1. 1. 오전 9:00:00"
                                                }
                                                title="STARTED AT"
                                            />
                                        </section>
                                    </div>
                                ) : (
                                    <div></div>
                                )}
                            </div>
                            <Commit round={round} />
                        </div>
                    ) : (
                        <div></div>
                    )}
                </div>
            </div>
        </>
    )
}
