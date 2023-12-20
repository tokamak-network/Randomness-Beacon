import SetUp from "../components/SetUp"
import Round from "../components/Round"
import Commit from "../components/Commit"
import GetWinner from "../components/GetWinner"
import Withdraw from "../components/Withdraw"
import { useMoralis } from "react-moralis"
import { useState, useEffect } from "react"
import { useWeb3Contract } from "react-moralis"
import { abi, contractAddresses } from "./../constants"
import { CountdownCircleTimer } from "react-countdown-circle-timer"
import { ethers, toBeHex } from "ethers"
import Moment from "react-moment"
import { useInterval } from "use-interval"
import RankOfEachParticipants from "../components/RankOfEachParticipants"

const supportedChains = ["31337", "11155111"]

export default function Home() {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const [nowTime, setNowTime] = useState(new Date())
    const chainId = parseInt(chainIdHex)
    const raffleAddress = chainId in contractAddresses ? contractAddresses[chainId][0] : null
    let [round, setRound] = useState(0)
    const [entranceFee, setEntranceFee] = useState(0)
    const [isSetUp, setIsSetUp] = useState(false)
    const [isCommit, setIsCommit] = useState(false)
    const [settedUpValues, setSettedUpValues] = useState({})
    const [started, setStarted] = useState("")
    const [participatedRounds, setParticipatedRounds] = useState([])

    useInterval(() => {
        setNowTime(new Date())
    }, 1000)
    useEffect(() => {
        if (isWeb3Enabled) {
            updateUI()
        }
    }, [isWeb3Enabled, round])
    useInterval(() => {
        updateUI()
    }, 12000)
    const { runContractFunction: setUpValuesAtRound } = useWeb3Contract()
    const { runContractFunction: raffleRound } = useWeb3Contract({
        abi: abi,
        contractAddress: raffleAddress, //,
        functionName: "raffleRound", //,
        params: {},
    })
    const { runContractFunction: getParticipatedRounds } = useWeb3Contract({
        abi: abi,
        contractAddress: raffleAddress, //,
        functionName: "getParticipatedRounds", //,
        params: {},
    })
    const { runContractFunction: entranceFeesAtRound } = useWeb3Contract()

    async function updateUI() {
        const roundFromCall = (
            await raffleRound({ onError: (error) => console.log(error) })
        ).toString()
        setRound(roundFromCall)
        const participatedRoundsfromCall = await getParticipatedRounds({
            onError: (error) => console.log(error),
        })
        let temp = []
        for (let i = 0; i < participatedRoundsfromCall.length; i++) {
            temp.push(participatedRoundsfromCall[i].toString())
        }
        setParticipatedRounds(temp)
        await getSetUpValuesAtRound(roundFromCall)
        await getEntranceFee()
        if (settedUpValues.setUpTime !== undefined && settedUpValues.setUpTime != "0") {
            setIsSetUp(true)
            setIsCommit(true)
            setStarted("Started!")
        } else {
            setIsSetUp(false)
            setIsCommit(true)
            setStarted("Not Started")
        }
    }
    async function getSetUpValuesAtRound(roundFromCall) {
        const setUpValuesAtRoundOptions = {
            abi: abi,
            contractAddress: raffleAddress,
            functionName: "setUpValuesAtRound",
            params: { round: roundFromCall },
        }
        const result = await setUpValuesAtRound({
            params: setUpValuesAtRoundOptions,
            onError: (error) => console.log(error),
        })
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
    async function getEntranceFee() {
        const setUpOptions = {
            abi: abi,
            contractAddress: raffleAddress,
            functionName: "entranceFeesAtRound",
            params: { round },
        }
        const result = await entranceFeesAtRound({
            params: setUpOptions,
            onError: (error) => console.log(error),
        })
        setEntranceFee(result)
    }
    return (
        <div className="bg-[url('../public/christmas_gift_boxes_background.png')] min-h-screen bg-repeat-y bg-cover bg-center">
            <div className="container mx-auto w-9/12 min-h-screen bg-yellow-50">
                <Round round={round} />

                {raffleAddress ? (
                    <div>
                        <div className="border-dashed border-amber-950 border-2 rounded-lg p-10 m-5 truncate hover:text-clip">
                            <div>Round: {round}</div>

                            <div>
                                {settedUpValues ? (
                                    <div>
                                        <div>
                                            commitDuration: {settedUpValues.commitDuration} seconds
                                        </div>
                                        <div>
                                            commit~revealDuration:{" "}
                                            {settedUpValues.commitRevealDuration} seconds
                                        </div>
                                        <div>
                                            setUp date -
                                            {new Date(
                                                settedUpValues.setUpTime * 1000
                                            ).toLocaleDateString()}
                                            {new Date(
                                                settedUpValues.setUpTime * 1000
                                            ).toLocaleTimeString()}
                                        </div>
                                    </div>
                                ) : (
                                    <div></div>
                                )}

                                <div>
                                    current date
                                    {nowTime.toLocaleDateString()}
                                    {nowTime.toLocaleTimeString()}
                                </div>
                                {settedUpValues ? (
                                    <div>
                                        <div>
                                            commit end time
                                            {new Date(
                                                settedUpValues.setUpTime * 1000 +
                                                    settedUpValues.commitDuration * 1000
                                            ).toLocaleDateString()}
                                            {new Date(
                                                settedUpValues.setUpTime * 1000 +
                                                    settedUpValues.commitDuration * 1000
                                            ).toLocaleTimeString()}
                                        </div>
                                    </div>
                                ) : (
                                    <div></div>
                                )}
                                <div>
                                    entranceFee: {ethers.formatEther(entranceFee.toString())} eth
                                </div>
                            </div>
                        </div>
                        {/* <div className="m-5">
                    <CountdownCircleTimer
                        isPlaying={isSetUp}
                        duration={isSetUp ? settedUpValues.commitDuration : 0}
                        initialRemainingTime={
                            isSetUp
                                ? settedUpValues.commitDuration -
                                  (Math.round(Date.now() / 1000) - settedUpValues.setUpTime)
                                : 0
                        }
                        colors={["#004777", "#F7B801", "#A30000", "#A30000"]}
                        colorsTime={[7, 5, 2, 0]}
                    >
                        {({ remainingTime }) => remainingTime}
                    </CountdownCircleTimer>
                    <div>Commit Remaining Time</div>
                </div> */}
                        <Commit commitIndex="0" entranceFee={entranceFee} />
                        <GetWinner round={round} participatedRounds={participatedRounds} />
                        <div>
                            <RankOfEachParticipants round={round} />
                        </div>
                    </div>
                ) : (
                    <div></div>
                )}
            </div>
        </div>
    )
}
