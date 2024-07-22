// Copyright 2024 justin
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
import { BigNumberish } from "ethers"
import { useEffect, useState } from "react"
import { useMoralis, useWeb3Contract } from "react-moralis"
import { useInterval } from "use-interval"
import { Footer } from "../components/Footer"
import { MainHeader } from "../components/MainComponents/MainHeader"
import { Register } from "../components/MainComponents/Register"
import { RequestTables } from "../components/MainComponents/RequestTables"
import { consumerContractAddress as consumerContractAddressJson, randomDayAbi } from "../constants"

export default function TempMain() {
    const { chainId: chainIdHex, isWeb3Enabled, account } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const contractAddresses: { [key: string]: string[] } = consumerContractAddressJson
    const consumerContractAddress =
        chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null
    const [timeRemaining, setTimeRemaining] = useState<string>("00:00:00")
    const [isEventOpen, setIsEventOpen] = useState<boolean>(false)
    const [avgNumber, setAvgNumber] = useState<BigNumberish>(0)
    const [requestIds, setRequestIds] = useState<BigNumberish[]>([])
    const [randomNums, setRandomNums] = useState<BigNumberish[]>([])
    const [threeClosestToSevenHundred, setThreeClosestToSevenHundred] = useState<any>([])
    const [startRegistrationTimeForNextRound, setStartRegistrationTimeForNextRound] =
        useState<string>("0")
    const [prettyStartRegistrationTimeForNextRound, setPrettyStartRegistrationTimeForNextRound] =
        useState<string>("1. 1. 오전 9:00:00")
    const [prettyRegistrationDurationForNextRound, setPrettyRegistrationDurationForNextRound] =
        useState<string>("00hrs 00min 00sec")
    const [registrationDurationForNextRound, setRegistrationDurationForNextRound] =
        useState<string>("0")
    function str_pad_left(string: number, pad: string, length: number) {
        return (new Array(length + 1).join(pad) + string).slice(-length)
    }
    // @ts-ignore
    const { runContractFunction: getRequestersInfos } = useWeb3Contract()
    // // @ts-ignore
    // const { runContractFunction: getWithdrawedRounds } = useWeb3Contract()
    // @ts-ignore
    // const { runContractFunction: getNextCryptoDiceRound } = useWeb3Contract({
    //     abi: cryptoDiceConsumerAbi,
    //     contractAddress: consumerContractAddress!, //,
    //     functionName: "getNextCryptoDiceRound", //,
    //     params: {},
    // })
    const { runContractFunction: eventEndTime } = useWeb3Contract({
        abi: randomDayAbi,
        contractAddress: consumerContractAddress!, //,
        functionName: "eventEndTime", //,
        params: {},
    })
    const { runContractFunction: getThreeClosestToSevenHundred } = useWeb3Contract({
        abi: randomDayAbi,
        contractAddress: consumerContractAddress!, //,
        functionName: "getThreeClosestToSevenHundred", //,
        params: {},
    })

    useInterval(() => {
        let registrationDurationForNextRoundInt = parseInt(registrationDurationForNextRound)
        if (parseInt(startRegistrationTimeForNextRound) > 0) {
            let _timeRemaing =
                registrationDurationForNextRoundInt -
                (Math.floor(Date.now() / 1000) - parseInt(startRegistrationTimeForNextRound))
            if (_timeRemaing > -1) {
                const hours = Math.floor(_timeRemaing / 3600)
                const minutes = Math.floor((_timeRemaing - hours * 3600) / 60)
                const seconds = _timeRemaing - hours * 3600 - minutes * 60
                setTimeRemaining(
                    str_pad_left(hours, "0", 2) +
                        ":" +
                        str_pad_left(minutes, "0", 2) +
                        ":" +
                        str_pad_left(seconds, "0", 2)
                )
                setIsEventOpen(true)
            } else {
                setIsEventOpen(false)
            }
        }
    }, 1000)
    useEffect(() => {
        if (isWeb3Enabled) {
            updateUI()
        }
    }, [isWeb3Enabled, account])
    useInterval(() => {
        updateUI()
    }, 11000)

    async function updateUI() {
        if (consumerContractAddress) {
            const eventDuration = 86400
            let registrationStartTime: BigNumberish = (await eventEndTime()) as BigNumberish
            if (Number(registrationStartTime) > 0)
                registrationStartTime = (Number(registrationStartTime) -
                    eventDuration) as BigNumberish
            let registrationDuration: BigNumberish = eventDuration
            setRegistrationDurationForNextRound(registrationDuration.toString())
            const hours = Math.floor(parseInt(registrationDuration.toString()) / 3600)
            const minutes = Math.floor(
                (parseInt(registrationDuration.toString()) - hours * 3600) / 60
            )
            const seconds = parseInt(registrationDuration.toString()) - hours * 3600 - minutes * 60
            setPrettyRegistrationDurationForNextRound(
                str_pad_left(hours, "0", 2) +
                    "hrs " +
                    str_pad_left(minutes, "0", 2) +
                    "min " +
                    str_pad_left(seconds, "0", 2) +
                    "sec"
            )
            setStartRegistrationTimeForNextRound(registrationStartTime.toString())
            setPrettyStartRegistrationTimeForNextRound(
                new Date(Number(registrationStartTime.toString()) * 1000).toLocaleString().slice(5)
            )
            const getRequestersInfosOptions = {
                abi: randomDayAbi,
                contractAddress: consumerContractAddress!,
                functionName: "getRequestersInfos",
                params: { requester: account },
            }
            const getRequestersInfosResult: any = await getRequestersInfos({
                params: getRequestersInfosOptions,
                onError: (error) => console.log(error),
            })
            setAvgNumber(getRequestersInfosResult[0])
            setRequestIds(getRequestersInfosResult[1])
            setRandomNums(getRequestersInfosResult[2])
            const getThreeClosestToSevenHundredResult = await getThreeClosestToSevenHundred()
            setThreeClosestToSevenHundred(getThreeClosestToSevenHundredResult)
            // const participantsLengthfromCallOptions = {
            //     abi: cryptoDiceConsumerAbi,
            //     contractAddress: consumerContractAddress!,
            //     functionName: "getRegisteredCount",
            //     params: { round: currentRound },
            // }
            // const participantsLengthfromCall = (await getRegisteredCount({
            //     params: participantsLengthfromCallOptions,
            //     onError: (error) => console.log(error),
            // })) as BigNumberish
        }
    }

    return (
        <>
            {" "}
            <MainHeader />
            <Register
                timeRemaining={timeRemaining}
                registrationDurationForNextRound={prettyRegistrationDurationForNextRound}
                startRegistrationTimeForNextRound={prettyStartRegistrationTimeForNextRound}
                updateUI={updateUI}
                isEventOpen={isEventOpen}
                averageNumber={avgNumber}
            />
            <div>
                <RequestTables
                    requestIds={requestIds}
                    randomNums={randomNums}
                    threeClosestToSevenHundred={threeClosestToSevenHundred}
                />
            </div>
            {/* <div>
                <RankOfEachParticipantsMain
                    round={round}
                    participatedRounds={participatedRounds}
                    withdrawedRounds={withdrawedRounds}
                    updateUI={updateUI}
                />
            </div>  */}
            <Footer />
        </>
    )
}
