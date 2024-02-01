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
import { MainHeader } from "../components/MainComponents/MainHeader"
import { Register } from "../components/MainComponents/Register"
import { useWeb3Contract } from "react-moralis"
import { useInterval } from "use-interval"
import { useNotification, Bell } from "web3uikit"
import RankOfEachParticipantsMain from "../components/MainComponents/RankOfEachParticipantsMain"
import { useMoralis } from "react-moralis"
import { Footer } from "../components/Footer"
import { useState, useEffect } from "react"
import { BigNumber, BigNumberish, ethers } from "ethers"
import { abi, contractAddresses as contractAddressesJSON } from "../constants"
export default function TempMain() {
    const { chainId: chainIdHex, isWeb3Enabled, account } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const contractAddresses: { [key: string]: string[] } = contractAddressesJSON
    const randomAirdropAddress =
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
        useState<string>("")
    const dispatch = useNotification()
    function str_pad_left(string: number, pad: string, length: number) {
        return (new Array(length + 1).join(pad) + string).slice(-length)
    }
    // @ts-ignore
    const { runContractFunction: registerNextRound, isLoading } = useWeb3Contract()
    const [isFetching, setIsFetching] = useState(false)
    // @ts-ignore
    const { runContractFunction: getParticipantsLengthAtRound } = useWeb3Contract()
    const { runContractFunction: getNextRound } = useWeb3Contract({
        abi: abi,
        contractAddress: randomAirdropAddress!, //,
        functionName: "getNextRound", //,
        params: {},
    })
    const {
        runContractFunction: getRegistrationDurationForNextRound, //
    } = useWeb3Contract({
        abi: abi,
        contractAddress: randomAirdropAddress!, //,
        functionName: "getRegistrationDurationForNextRound", //,
        params: {},
    })
    const { runContractFunction: getStartRegistrationTimeForNextRound } = useWeb3Contract({
        abi: abi,
        contractAddress: randomAirdropAddress!, //,
        functionName: "getStartRegistrationTimeForNextRound", //,
        params: {},
    })
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
        if (randomAirdropAddress) {
            let registrationDurationForNextRoundFromCall =
                (await getRegistrationDurationForNextRound()) as BigNumberish
            let startRegistrationTimeForNextRoundFromCall =
                (await getStartRegistrationTimeForNextRound()) as BigNumberish
            let roundFromCall = (await randomAirdropRound({
                onError: (error) => console.log(error),
            })) as BigNumberish
            let nextRoundFromCall = (await getNextRound({
                onError: (error) => console.log(error),
            })) as BigNumberish
            setRegistrationDurationForNextRound(
                registrationDurationForNextRoundFromCall?.toString()
            )
            const hours = Math.floor(
                parseInt(registrationDurationForNextRoundFromCall?.toString()) / 3600
            )
            const minutes = Math.floor(
                (parseInt(registrationDurationForNextRoundFromCall?.toString()) - hours * 3600) /
                    60
            )
            const seconds =
                parseInt(registrationDurationForNextRoundFromCall?.toString()) -
                hours * 3600 -
                minutes * 60
            setPrettyRegistrationDurationForNextRound(
                str_pad_left(hours, "0", 2) +
                    "hrs " +
                    str_pad_left(minutes, "0", 2) +
                    "min " +
                    str_pad_left(seconds, "0", 2) +
                    "sec"
            )
            setStartRegistrationTimeForNextRound(
                startRegistrationTimeForNextRoundFromCall.toString()
            )
            setPrettyStartRegistrationTimeForNextRound(
                new Date(Number(startRegistrationTimeForNextRoundFromCall.toString()) * 1000)
                    .toLocaleString()
                    .slice(5)
            )
            setNextRound(nextRoundFromCall.toString())
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
                />
            </div>
            <Footer />
        </>
    )
}
