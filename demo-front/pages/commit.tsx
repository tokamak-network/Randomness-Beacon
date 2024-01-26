import Round from "../components/Round"
import Commit from "../components/Commit"
import { useMoralis } from "react-moralis"
import { useState, useEffect } from "react"
import { useWeb3Contract } from "react-moralis"
import { abi, contractAddresses as contractAddressesJSON } from "../constants"
import { useInterval } from "use-interval"
import { Widget } from "web3uikit"
import { ICommitRevealRecoverRNG } from "../typechain-types/RandomAirdrop"
import { BigNumber, BigNumberish } from "ethers"
import Header from "../components/Header"
import { SettedUpValues } from "../typechain-types/RandomAirdrop"

export default function Home() {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex!).toString()
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
        if (roundFromCall === undefined) roundFromCall = BigNumber.from(0)
        setRound(roundFromCall.toString())
        const participatedRoundsfromCall: BigNumber[] = (await getParticipatedRounds({
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
        if (settedUpValues.setUpTime !== undefined && settedUpValues.setUpTime != "0") {
            setStarted("Started!")
        } else {
            setStarted("Not Started")
        }
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
                    className="bg-white	container mx-auto w-6/12 rounded-3xl border-dashed border-amber-950 border-2"
                >
                    <Round round={round} />
                    {randomAirdropAddress ? (
                        <div>
                            <div className="border-dashed border-amber-950 border-2 rounded-lg m-5 truncate hover:text-clip ">
                                <div className="mt-10 ml-10 font-bold">Current Round Info</div>
                                {settedUpValues ? (
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
                                                    str_pad_left(
                                                        Math.floor(
                                                            parseInt(
                                                                settedUpValues.commitDuration
                                                            ) / 60
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
                                                info={new Date(
                                                    Number(settedUpValues.setUpTime) * 1000
                                                )
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
