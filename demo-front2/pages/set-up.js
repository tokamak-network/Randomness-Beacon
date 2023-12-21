import SetUp from "../components/SetUp"
import Round from "../components/Round"
import Commit from "../components/Commit"
import GetWinner from "../components/GetWinner"
import Withdraw from "../components/Withdraw"
import { useMoralis } from "react-moralis"
import { useState, useEffect } from "react"
import { useWeb3Contract } from "react-moralis"
import { abi, contractAddresses } from "./../constants"
import Recover from "../components/Recover"
import Moment from "react-moment"
import { useInterval } from "use-interval"
import { CountdownCircleTimer } from "react-countdown-circle-timer"

const supportedChains = ["31337", "11155111"]

export default function SetUpPage() {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const [nowTime, setNowTime] = useState(new Date())
    const chainId = parseInt(chainIdHex)
    const raffleAddress = chainId in contractAddresses ? contractAddresses[chainId][0] : null

    let [round, setRound] = useState(0)
    const [isSetUp, setIsSetUp] = useState(false)
    const [isCommit, setIsCommit] = useState(false)
    const [settedUpValues, setSettedUpValues] = useState({})
    const [started, setStarted] = useState("")
    useInterval(() => {
        setNowTime(new Date())
    }, 1000)
    useEffect(() => {
        if (isWeb3Enabled) {
            updateUI()
        }
    }, [isWeb3Enabled, round])

    const { runContractFunction: setUpValuesAtRound } = useWeb3Contract()

    const { runContractFunction: raffleRound } = useWeb3Contract({
        abi: abi,
        contractAddress: raffleAddress, //,
        functionName: "raffleRound", //,
        params: {},
    })

    async function updateUI() {
        const roundFromCall = (
            await raffleRound({ onError: (error) => console.log(error) })
        ).toString()
        setRound(roundFromCall)
        await getSetUpValuesAtRound(roundFromCall)
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
        roundFromCall = parseInt(roundFromCall)
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
    return (
        <div>
            <div className="container mx-auto">
                <Round round={round} />
                {raffleAddress ? (
                    <div>
                        <div className="border-dashed border-amber-950 border-2 rounded-lg p-10 m-5 truncate hover:text-clip">
                            <div>Round: {round}</div>
                            <div>T: {settedUpValues.T}</div>
                            <div>n: {settedUpValues.n}</div>
                            <div>g: {settedUpValues.g}</div>
                            <div>h: {settedUpValues.h}</div>
                            <div>commitDuration: {settedUpValues.commitDuration} seconds</div>
                            <div>
                                commitRevealDuration: {settedUpValues.commitRevealDuration} seconds
                            </div>
                            <div>setUpTime: {settedUpValues.setUpTime}</div>
                            <div>
                                setUp date -
                                {new Date(settedUpValues.setUpTime * 1000).toLocaleDateString()}
                                {new Date(settedUpValues.setUpTime * 1000).toLocaleTimeString()}
                            </div>
                            <div>
                                current date
                                {nowTime.toLocaleDateString()}
                                {nowTime.toLocaleTimeString()}
                            </div>
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
                        {/* <div className="m-10">
                    <CountdownCircleTimer
                        isPlaying={isCommit}
                        duration={isSetUp ? settedUpValues.commitDuration : 0}
                        initialRemainingTime={
                            isSetUp
                                ? settedUpValues.commitDuration -
                                      (Math.round(Date.now() / 1000) - settedUpValues.setUpTime) >
                                  0
                                    ? settedUpValues.commitDuration -
                                      (Math.round(Date.now() / 1000) - settedUpValues.setUpTime)
                                    : 0
                                : 0
                        }
                        onComplete={() => {
                            setIsCommit(false)
                            setStarted("Not Started")
                        }}
                        colors={["#004777", "#F7B801", "#A30000", "#A30000"]}
                        colorsTime={[7, 5, 2, 0]}
                    >
                        {({ remainingTime }) => remainingTime}
                    </CountdownCircleTimer>
                    <div>Commit Remaining Time</div>
                </div> */}
                        <SetUp updateUI={updateUI} isSetUp={isSetUp} />
                        <Recover round={round} />
                    </div>
                ) : (
                    <div>...</div>
                )}
            </div>
        </div>
    )
}
