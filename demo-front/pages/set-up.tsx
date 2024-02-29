import { BigNumber, BigNumberish } from "ethers"
import { useEffect, useState } from "react"
import { useMoralis, useWeb3Contract } from "react-moralis"
import { useInterval } from "use-interval"
import Header from "../components/Header"
import Recover from "../components/Recover"
import Round from "../components/Round"
import StartRegistration from "../components/StartRegistration"
import {
    airdropConsumerAbi,
    consumerContractAddress as consumerContractAddressJSON,
    coordinatorContractAddress as coordinatorContractAddressJSON,
    crrngAbi,
} from "../constants"
/*
        uint256 startTime;
        uint256 numOfPariticipants;
        uint256 count; //This variable is used to keep track of the number of commitments and reveals, and to check if anything has been committed when moving to the reveal stage.
        address consumer;
        bytes bStar; // hash of commitsString
        bytes commitsString; // concatenated string of commits
        BigNumber omega; // the random number
        Stages stage; // stage of the contract
        bool isCompleted; // omega is finialized when this is true
        bool isAllRevealed; // true when all participants have revealed
*/
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

export default function SetUpPage() {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const [nowTime, setNowTime] = useState<Date>()
    const chainId = parseInt(chainIdHex!)
    const consumerContractAddresses: { [key: string]: string[] } = consumerContractAddressJSON
    const coordinatorContractAddresses: { [key: string]: string[] } =
        coordinatorContractAddressJSON
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
    const randomAirdropAddress =
        !isNaN(chainId) && chainId in consumerContractAddresses
            ? consumerContractAddresses[chainId][consumerContractAddresses[chainId].length - 1]
            : null
    const coordinatorAddress =
        !isNaN(chainId) && chainId in coordinatorContractAddresses
            ? coordinatorContractAddresses[chainId][
                  coordinatorContractAddresses[chainId].length - 1
              ]
            : null

    let [round, setRound] = useState<string>("")
    const [setUpValues, setSetUpValues] = useState<
        [BigNumberish, BigNumberish, BigNumberish, string, string, string]
    >([0, 0, 0, "", "", ""])
    useInterval(() => {
        setNowTime(new Date())
    }, 1000)
    useEffect(() => {
        if (isWeb3Enabled) {
            updateUI()
        }
    }, [isWeb3Enabled, round])
    const { runContractFunction: getSetUpValues } = useWeb3Contract({
        abi: crrngAbi,
        contractAddress: coordinatorAddress!,
        functionName: "getSetUpValues",
        params: {},
    })

    const { runContractFunction: getNextRandomAirdropRound } = useWeb3Contract({
        abi: airdropConsumerAbi,
        contractAddress: randomAirdropAddress!, //,
        functionName: "getNextRandomAirdropRound", //,
        params: {},
    })

    // @ts-ignore
    const { runContractFunction: getValuesAtRound } = useWeb3Contract()

    async function updateUI() {
        const roundFromCall = (await getNextRandomAirdropRound({
            onError: (error) => console.log(error),
        })) as BigNumberish
        const roundInt =
            parseInt(roundFromCall.toString()) == 0 ? 0 : parseInt(roundFromCall.toString()) - 1
        setRound(roundInt.toString())
        await getGetSetUpValuesAtRound(roundInt)
    }
    async function getGetSetUpValuesAtRound(roundFromCall: BigNumberish) {
        const result = await getSetUpValues({
            onError: (error) => console.log(error),
        })
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
        if (result === undefined) return
        setSetUpValues(
            result as [BigNumberish, BigNumberish, BigNumberish, string, string, string]
        )
        setValuesAtRound(valuesAtRoundFromCall)
    }
    return (
        <>
            <Header />
            <div className="bg-slate-50 py-10">
                <div className="w-6/12 container mx-auto bg-white rounded-3xl border-dashed border-slate-300 border-2">
                    <Round round={round} />
                    {randomAirdropAddress ? (
                        <div>
                            <div className="border-dashed border-slate-300 border-2 rounded-lg p-10 m-5 truncate hover:text-clip">
                                <div key="Round">Round: {round}</div>
                                <div key="T">T: 4194304</div>
                                <div key="n">n: {setUpValues[3]}</div>
                                <div key="g">g: {setUpValues[4]}</div>
                                <div key="h">h: {setUpValues[5]}</div>
                                <div key="commitDuration">commitDuration: 120 seconds</div>
                                <div key="commitRevealDuration">
                                    commitRevealDuration: 240 seconds
                                </div>
                                <div key="setUpTime">
                                    setUpTime: {valuesAtRound.startTime.toString()}
                                </div>
                                <div key="setUpDate">
                                    setUp date -
                                    {new Date(
                                        parseInt(valuesAtRound.startTime.toString()) * 1000
                                    ).toLocaleDateString()}
                                    {new Date(
                                        parseInt(valuesAtRound.startTime.toString()) * 1000
                                    ).toLocaleTimeString()}
                                </div>
                                <div key="current date">
                                    current date
                                    {nowTime ? nowTime.toLocaleDateString() : ""}
                                    {nowTime ? nowTime.toLocaleTimeString() : ""}
                                </div>
                                <div key="commitEndTime">
                                    commit end time
                                    {new Date(
                                        parseInt(valuesAtRound.startTime.toString()) * 1000 +
                                            120 * 1000
                                    ).toLocaleDateString()}
                                    {new Date(
                                        parseInt(valuesAtRound.startTime.toString()) * 1000 +
                                            120 * 1000
                                    ).toLocaleTimeString()}
                                </div>
                            </div>
                            <StartRegistration updateUI={updateUI} />
                            {/* <SetUp updateUI={updateUI} key="Setup" /> */}
                            <Recover round={round} />
                        </div>
                    ) : (
                        <div>...</div>
                    )}
                </div>
            </div>
        </>
    )
}
