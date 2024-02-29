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
import { BigNumber, BigNumberish } from "ethers"
import { useEffect, useState } from "react"
import { useMoralis, useWeb3Contract } from "react-moralis"
import { useInterval } from "use-interval"
import { useNotification } from "web3uikit"
import { Footer } from "../components/Footer"
import { MainHeader } from "../components/MainComponents/MainHeader"
import RankOfEachParticipantsMain from "../components/MainComponents/RankOfEachParticipantsMain"
import { Register } from "../components/MainComponents/Register"
import {
    airdropConsumerAbi,
    consumerContractAddress as consumerContractAddressJson,
} from "../constants"
export default function TempMain() {
    const { chainId: chainIdHex, isWeb3Enabled, account } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const contractAddresses: { [key: string]: string[] } = consumerContractAddressJson
    const consumerContractAddress =
        chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null
    let [round, setRound] = useState<string>("")
    const [timeRemaining, setTimeRemaining] = useState<string>("00:00:00")
    const [participatedRoundsLength, setParticipatedRoundsLength] = useState<string>("0")
    const [participatedRounds, setParticipatedRounds] = useState<string[]>([])
    const [nextRound, setNextRound] = useState<string>("")
    const [isRegistrationOpen, setIsRegistrationOpen] = useState<boolean>(false)
    const [startRegistrationTimeForNextRound, setStartRegistrationTimeForNextRound] =
        useState<string>("0")
    const [prettyStartRegistrationTimeForNextRound, setPrettyStartRegistrationTimeForNextRound] =
        useState<string>("1. 1. 오전 9:00:00")
    const [prettyRegistrationDurationForNextRound, setPrettyRegistrationDurationForNextRound] =
        useState<string>("00hrs 00min 00sec")
    const [registrationDurationForNextRound, setRegistrationDurationForNextRound] =
        useState<string>("0")
    const [withdrawedRounds, setWithdrawedRounds] = useState<string[]>([])
    const dispatch = useNotification()
    function str_pad_left(string: number, pad: string, length: number) {
        return (new Array(length + 1).join(pad) + string).slice(-length)
    }
    // @ts-ignore
    const { runContractFunction: registerNextRound } = useWeb3Contract()
    // @ts-ignore
    const { runContractFunction: getWithdrawedRounds } = useWeb3Contract()
    // @ts-ignore
    const { runContractFunction: getNumOfParticipants } = useWeb3Contract()
    const { runContractFunction: getNextRandomAirdropRound } = useWeb3Contract({
        abi: airdropConsumerAbi,
        contractAddress: consumerContractAddress!, //,
        functionName: "getNextRandomAirdropRound", //,
        params: {},
    })
    const {
        runContractFunction: getRegistrationTimeAndDuration, //
    } = useWeb3Contract({
        abi: airdropConsumerAbi,
        contractAddress: consumerContractAddress!, //,
        functionName: "getRegistrationTimeAndDuration", //,
        params: {},
    })
    // @ts-ignore
    const { runContractFunction: getParticipatedRounds } = useWeb3Contract()
    useInterval(() => {
        let registrationDurationForNextRoundInt = parseInt(registrationDurationForNextRound)
        if (registrationDurationForNextRoundInt > 0) {
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
                setIsRegistrationOpen(true)
            } else {
                setIsRegistrationOpen(false)
            }
        }
    }, 1000)
    useEffect(() => {
        if (isWeb3Enabled) {
            updateUI()
        }
    }, [isWeb3Enabled, round, account])
    useInterval(() => {
        updateUI()
    }, 11000)

    async function updateUI() {
        if (consumerContractAddress) {
            let registrationTimeAndDurationfromCall: [BigNumberish, BigNumberish] =
                (await getRegistrationTimeAndDuration()) as [BigNumberish, BigNumberish]
            let registrationStartTime: BigNumberish = registrationTimeAndDurationfromCall[0]
            let registrationDuration: BigNumberish = registrationTimeAndDurationfromCall[1]
            let nextRoundFromCall = (await getNextRandomAirdropRound({
                onError: (error) => console.log(error),
            })) as BigNumberish
            let currentRound: Number =
                Number(nextRoundFromCall.toString()) == 0
                    ? 0
                    : Number(nextRoundFromCall.toString()) - 1
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
            setNextRound(currentRound.toString())
            setRound(currentRound.toString())
            const participantsLengthfromCallOptions = {
                abi: airdropConsumerAbi,
                contractAddress: consumerContractAddress!,
                functionName: "getNumOfParticipants",
                params: { round: currentRound },
            }
            const participantsLengthfromCall = (await getNumOfParticipants({
                params: participantsLengthfromCallOptions,
                onError: (error) => console.log(error),
            })) as BigNumberish
            setParticipatedRoundsLength(participantsLengthfromCall?.toString())
            const participatedRoundsfromCallOptions = {
                abi: airdropConsumerAbi,
                contractAddress: consumerContractAddress!,
                functionName: "getParticipatedRounds",
                params: { participantAddress: account },
            }
            const participatedRoundsfromCall = (await getParticipatedRounds({
                params: participatedRoundsfromCallOptions,
                onError: (error) => console.log(error),
            })) as BigNumber[]
            const getWithdrawedRoundsOptions = {
                abi: airdropConsumerAbi,
                contractAddress: consumerContractAddress!,
                functionName: "getWithdrawedRounds",
                params: { participant: account },
            }
            const getWithdrawedRoundsOptionsfromCall = (await getWithdrawedRounds({
                params: getWithdrawedRoundsOptions,
                onError: (error) => console.log(error),
            })) as BigNumberish[]
            let temp = []
            let temp2 = []

            if (participatedRoundsfromCall) {
                for (let i = 0; i < participatedRoundsfromCall.length; i++) {
                    temp.push(participatedRoundsfromCall[i].toString())
                }
                setParticipatedRounds(temp)
            }
            if (getWithdrawedRoundsOptionsfromCall) {
                for (let i = 0; i < getWithdrawedRoundsOptionsfromCall.length; i++) {
                    temp2.push(getWithdrawedRoundsOptionsfromCall[i].toString())
                }
                setWithdrawedRounds(temp2)
            }
        }
    }

    return (
        <>
            {" "}
            <MainHeader />
            <Register
                participatedRoundsLength={participatedRoundsLength}
                timeRemaining={timeRemaining}
                registrationDurationForNextRound={prettyRegistrationDurationForNextRound}
                startRegistrationTimeForNextRound={prettyStartRegistrationTimeForNextRound}
                round={nextRound}
                updateUI={updateUI}
                isRegistrationOpen={isRegistrationOpen}
                isRegistered={participatedRounds.includes(nextRound)}
            />
            <div>
                <RankOfEachParticipantsMain
                    round={round}
                    participatedRounds={participatedRounds}
                    withdrawedRounds={withdrawedRounds}
                    updateUI={updateUI}
                />
            </div>
            <Footer />
        </>
    )
}
