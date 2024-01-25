import SetUp from "../components/SetUp"
import Round from "../components/Round"
import { useMoralis } from "react-moralis"
import { useState, useEffect } from "react"
import { useWeb3Contract } from "react-moralis"
import { abi, contractAddresses as randomAirdropAddressJSON } from "../constants"
import Recover from "../components/Recover"
import { useInterval } from "use-interval"
import {BigNumberish} from "ethers"
import { SettedUpValues } from "../typechain-types/RandomAirdrop"
import {ICommitRevealRecoverRNG} from "../typechain-types/RandomAirdrop"

export default function SetUpPage() {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const [nowTime, setNowTime] = useState(new Date())
    const chainId = parseInt(chainIdHex!)
    const contractAddresses: { [key: string]: string[] } = randomAirdropAddressJSON
    const randomAirdropAddress =
        chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null

    let [round, setRound] = useState<string>("")
    const [isSetUp, setIsSetUp] = useState(false)
    const [isCommit, setIsCommit] = useState(false)
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
    const [started, setStarted] = useState("")
    useInterval(() => {
        setNowTime(new Date())
    }, 1000)
    useEffect(() => {
        if (isWeb3Enabled) {
            updateUI()
        }
    }, [isWeb3Enabled, round])
    // @ts-ignore
    const { runContractFunction: getSetUpValuesAtRound } = useWeb3Contract()

    const { runContractFunction: randomAirdropRound } = useWeb3Contract({
        abi: abi,
        contractAddress: randomAirdropAddress!, //,
        functionName: "randomAirdropRound", //,
        params: {},
    })

    async function updateUI() {
        const roundFromCall = (
            await randomAirdropRound({ onError: (error) => console.log(error) })
        ) as BigNumberish
        setRound(roundFromCall.toString())
        await getGetSetUpValuesAtRound(roundFromCall)
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
    async function getGetSetUpValuesAtRound(roundFromCall:BigNumberish) {
        const setUpValuesAtRoundOptions = {
            abi: abi,
            contractAddress: randomAirdropAddress!,
            functionName: "getSetUpValuesAtRound",
            params: { _round: roundFromCall },
        }
        const result:ICommitRevealRecoverRNG.SetUpValueAtRoundStructOutput = await getSetUpValuesAtRound({
            params: setUpValuesAtRoundOptions,
            onError: (error) => console.log(error),
        }) as ICommitRevealRecoverRNG.SetUpValueAtRoundStructOutput
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
        <div className="bg-slate-50 py-10">
            <div className="w-6/12 container mx-auto bg-white rounded-3xl border-dashed border-amber-950 border-2">
                <Round round={round} />
                {randomAirdropAddress ? (
                    <div>
                        <div className="border-dashed border-amber-950 border-2 rounded-lg p-10 m-5 truncate hover:text-clip">
                            <div key="Round">Round: {round}</div>
                            <div key="T">T: {settedUpValues.T}</div>
                            <div key="n">n: {settedUpValues.n}</div>
                            <div key="g">g: {settedUpValues.g}</div>
                            <div key="h">h: {settedUpValues.h}</div>
                            <div key="commitDuration">commitDuration: {settedUpValues.commitDuration} seconds</div>
                            <div key="commitRevealDuration">
                                commitRevealDuration: {settedUpValues.commitRevealDuration} seconds
                            </div>
                            <div key="setUpTime">setUpTime: {settedUpValues.setUpTime}</div>
                            <div key="setUpDate">
                                setUp date -
                                {new Date(parseInt(settedUpValues.setUpTime)* 1000).toLocaleDateString()}
                                {new Date(parseInt(settedUpValues.setUpTime)* 1000).toLocaleTimeString()}
                            </div>
                            <div key="current date">
                                current date
                                {nowTime.toLocaleDateString()}
                                {nowTime.toLocaleTimeString()}
                            </div>
                            <div key="commitEndTime">
                                commit end time
                                {new Date(
                                    parseInt(settedUpValues.setUpTime) * 1000 +
                                    parseInt(settedUpValues.commitDuration) * 1000
                                ).toLocaleDateString()}
                                {new Date(
                                    parseInt(settedUpValues.setUpTime) * 1000 +
                                    parseInt(settedUpValues.commitDuration) * 1000
                                ).toLocaleTimeString()}
                            </div>
                        </div>
                        <SetUp updateUI={updateUI} key="Setup"/>
                        <Recover round={round} />
                    </div>
                ) : (
                    <div>...</div>
                )}
            </div>
        </div>
    )
}
