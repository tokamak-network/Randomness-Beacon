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
import { Widget } from "web3uikit"
import RankOfEachParticipants from "../components/RankOfEachParticipants"

const supportedChains = ["31337", "11155111"]

export default function Home() {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex)
    const raffleAddress = chainId in contractAddresses ? contractAddresses[chainId][0] : null
    let [round, setRound] = useState(0)
    const [isSetUp, setIsSetUp] = useState(false)
    const [isCommit, setIsCommit] = useState(false)
    const [settedUpValues, setSettedUpValues] = useState({})
    const [timeRemaining, setTimeRemaining] = useState(0)
    const [started, setStarted] = useState("")
    const [participatedRounds, setParticipatedRounds] = useState([])
    function str_pad_left(string, pad, length) {
        return (new Array(length + 1).join(pad) + string).slice(-length)
    }
    useInterval(() => {
        let commitDurationInt
        if (settedUpValues.commitDuration) {
            commitDurationInt = parseInt(settedUpValues.commitDuration)
            if (commitDurationInt > 0) {
                let _timeRemaing =
                    commitDurationInt -
                    (Math.floor(Date.now() / 1000) - parseInt(settedUpValues.setUpTime))
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

    async function updateUI() {
        const roundFromCall = await raffleRound({ onError: (error) => console.log(error) })
        if (roundFromCall === undefined) roundFromCall = 0
        setRound(roundFromCall.toString())
        const participatedRoundsfromCall = await getParticipatedRounds({
            onError: (error) => console.log(error),
        })
        let temp = []
        for (let i = 0; i < participatedRoundsfromCall.length; i++) {
            temp.push(participatedRoundsfromCall[i].toString())
        }
        setParticipatedRounds(temp)
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
    function fancyTimeFormat(duration) {
        // Hours, minutes and seconds
        const hrs = ~~(duration / 3600)
        const mins = ~~((duration % 3600) / 60)
        const secs = ~~duration % 60

        // Output like "1:01" or "4:03:59" or "123:03:59"
        let ret = ""

        if (hrs > 0) {
            ret += "" + hrs + ":" + (mins < 10 ? "0" : "")
        }

        ret += "" + mins + ":" + (secs < 10 ? "0" : "")
        ret += "" + secs

        return ret
    }
    return (
        <div className="bg-[url('../public/christmas_gift_boxes_background.png')] opacity-80 min-h-screen bg-repeat-y bg-cover bg-center py-10">
            <div
                style={{ minWidth: "852px" }}
                className="container mx-auto w-5/12 rounded-3xl bg-green-50 "
            >
                <Round round={round} />
                {raffleAddress ? (
                    <div>
                        <div className="border-dashed border-amber-950 border-2 rounded-lg m-5 truncate hover:text-clip ">
                            <div className="mt-10 ml-10 font-bold">Current Round Info</div>
                            {settedUpValues ? (
                                <div
                                    style={{ display: "grid", gap: "20px", padding: "40px 20px" }}
                                >
                                    <section style={{ display: "flex", gap: "20px" }}>
                                        <Widget
                                            style={{ backgroundColor: "rgb(236 253 245)" }}
                                            info={timeRemaining}
                                            title="TIME REMAINING"
                                        />

                                        <Widget
                                            style={{ backgroundColor: "rgb(236 253 245)" }}
                                            info={
                                                str_pad_left(
                                                    Math.floor(
                                                        parseInt(settedUpValues.commitDuration) /
                                                            60
                                                    ),
                                                    "0",
                                                    2
                                                ) +
                                                " min, " +
                                                str_pad_left(
                                                    parseInt(settedUpValues.commitDuration) -
                                                        Math.floor(
                                                            parseInt(
                                                                settedUpValues.commitDuration
                                                            ) / 60
                                                        ) *
                                                            60,
                                                    "0",
                                                    2
                                                ) +
                                                " sec"
                                            }
                                            title="COMMIT DURATION"
                                        ></Widget>
                                        <Widget
                                            style={{ backgroundColor: "rgb(236 253 245)" }}
                                            info={new Date(settedUpValues.setUpTime * 1000)
                                                .toLocaleString()
                                                .slice(5)}
                                            title="STARTED AT"
                                        />
                                    </section>
                                </div>
                            ) : (
                                <div></div>
                            )}
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
                        <Commit commitIndex="0" />
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
    )
}
