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
import { ethers } from "ethers"
import { decodeError } from "ethers-decode-error"
import { useRef, useState } from "react"
import Dice from "react-dice-roll"
import { useMoralis } from "react-moralis"
import { Bell, Input, useNotification } from "web3uikit"
import {
    consumerContractAddress as consumerContractAddressJSON,
    cryptoDiceConsumerAbi,
} from "../../constants"
import { BackgroundImage } from "./BackgroundImage"
import { Button } from "./Button"
import { Container } from "./Container"
declare type TValue = 1 | 2 | 3 | 4 | 5 | 6
declare type TDiceRef = {
    rollDice: (value: TValue) => void
}
export function Register({
    participatedRoundsLength,
    timeRemaining,
    registrationDurationForNextRound,
    startRegistrationTimeForNextRound,
    round,
    updateUI,
    isRegistrationOpen,
    isRegistered,
}: {
    participatedRoundsLength: string
    timeRemaining: string
    registrationDurationForNextRound: string
    startRegistrationTimeForNextRound: string
    round: string
    updateUI: () => Promise<void>
    isRegistrationOpen: boolean
    isRegistered: boolean
}) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const [diceDataState, setDiceDataState] = useState<
        "error" | "initial" | "disabled" | "confirmed" | undefined
    >("initial")
    const [isFetching, setIsFetching] = useState<boolean>(false)
    const contractAddresses: { [key: string]: string[] } = consumerContractAddressJSON
    const [diceNumber, setDiceNumber] = useState<number>()
    const randomAirdropAddress =
        !isNaN(chainId) && chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null
    const dispatch = useNotification()
    function validation() {
        if (diceNumber == undefined || diceNumber < 1 || diceNumber > 6) {
            setDiceDataState("error")
            dispatch({
                type: "error",
                message: "Invalid Dice Number Value",
                title: "Error Message",
                position: "topR",
                icon: <Bell />,
            })
            return false
        }
        return true
    }
    async function registerFunction() {
        if (validation()) {
            setIsFetching(true)
            const provider = new ethers.providers.Web3Provider((window as any).ethereum, "any")
            // Prompt user for account connections
            await provider.send("eth_requestAccounts", [])
            const signer = provider.getSigner()
            const randomAirdropContract = new ethers.Contract(
                randomAirdropAddress!,
                cryptoDiceConsumerAbi,
                provider
            )
            try {
                const tx = await randomAirdropContract
                    .connect(signer)
                    .register(diceNumber, { gasLimit: 150000 })
                await handleSuccess(tx)
            } catch (error: any) {
                console.log(error.message)
                const decodedError = decodeError(decodeError(error))
                dispatch({
                    type: "error",
                    message: decodedError.error,
                    title: "Error Message",
                    position: "topR",
                    icon: <Bell />,
                })
                setIsFetching(false)
            }
        }
    }
    const handleSuccess = async function (tx: any) {
        await tx.wait(1)
        handleNewNotification()
        setTimeout(() => {
            setIsFetching(false)
        }, 6000)
        await updateUI()
    }
    const handleNewNotification = function () {
        setTimeout(() => {
            dispatch({
                type: "info",
                message: "Transaction Completed",
                title: "Tx Notification",
                position: "topR",
                icon: <Bell />,
            })
        }, 6000)
    }
    const diceRef = useRef<TDiceRef>(null)
    const rollDice = (diceNum: TValue) => {
        diceRef.current?.rollDice(diceNum as TValue)
    }
    return (
        <div className="relative py-20 sm:pb-24 sm:pt-36">
            <BackgroundImage className="-bottom-14 -top-36 " />
            <Container className="relative pb-3.5">
                <div className="mx-auto max-w-2xl lg:max-w-4xl lg:px-12">
                    {randomAirdropAddress ? (
                        <>
                            {" "}
                            <h1 className="font-display text-5xl font-bold tracking-tighter text-blue-600 sm:text-7xl ">
                                Join TON Airdrop Event
                            </h1>
                            {isRegistrationOpen ? (
                                <div className="mt-6 space-y-6 font-display text-2xl tracking-tight text-blue-900">
                                    <div>
                                        You are submitting for round :{" "}
                                        <span className="font-semibold">{round}</span> , dice
                                        number :{" "}
                                        <span className="font-semibold">{diceNumber}</span>
                                    </div>
                                </div>
                            ) : (
                                <div className="mt-6 space-y-6 font-display text-2xl tracking-tight text-red-900">
                                    The submission of the dice number is closed
                                </div>
                            )}
                            <div className="mt-2 flex" style={{ alignItems: "center" }}>
                                <div className="flex-none mr-3">
                                    <Input
                                        label={"Enter a number of dice (1~6)"}
                                        type="number"
                                        placeholder="or roll the dice -------->"
                                        id="CommitValue"
                                        validation={{ required: true, numberMin: 1, numberMax: 6 }}
                                        value={diceNumber}
                                        onChange={(e) => {
                                            setDiceNumber(Number(e.target.value))
                                            setDiceDataState("initial")
                                            rollDice(Number(e.target.value) as TValue)
                                        }}
                                        state={diceDataState}
                                        errorMessage="Commit Value is required"
                                        width="13.5rem"
                                    />
                                </div>
                                <div className="flex-initial">
                                    <Dice
                                        faceBg="blue"
                                        size={65}
                                        ref={diceRef}
                                        onRoll={(value) => setDiceNumber(value)}
                                    />
                                </div>
                                {/* <button className="flex-1" onClick={rollDice}>
                                    Roll Dice
                                </button> */}
                                <div className="flex-1 ml-10 mb-11">
                                    <Button
                                        className={
                                            "mt-10 w-full " +
                                            (!isRegistrationOpen
                                                ? "opacity-20"
                                                : isRegistered
                                                ? "opacity-20"
                                                : "")
                                        }
                                        disabled={
                                            !isRegistrationOpen
                                                ? true
                                                : isRegistered
                                                ? true
                                                : false
                                        }
                                        onClick={registerFunction}
                                    >
                                        {isFetching ? (
                                            <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                                        ) : (
                                            <div>{isRegistered ? "Submitted!" : "Submit"}</div>
                                        )}
                                    </Button>
                                </div>
                            </div>
                            <dl className="mt-10 grid grid-cols-2 gap-x-10 gap-y-6 sm:mt-16 sm:gap-x-16 sm:gap-y-10 sm:text-center lg:auto-cols-auto lg:grid-flow-col lg:grid-cols-none lg:justify-start lg:text-left">
                                {[
                                    ["Submitted", participatedRoundsLength],
                                    ["Time Remaining", timeRemaining],
                                    ["Duration", registrationDurationForNextRound],
                                    [`Started At`, startRegistrationTimeForNextRound],
                                ].map(([name, value]) => (
                                    <div key={name}>
                                        <dt className="font-mono text-sm text-blue-600">{name}</dt>
                                        <dd className="mt-0.5 text-2xl font-semibold tracking-tight text-blue-900">
                                            {value}
                                        </dd>
                                    </div>
                                ))}
                            </dl>
                        </>
                    ) : (
                        <h2 className="py-4 px-4 font-bold text-2xl text-red-600 h-60">
                            Connect to Titan, Titan-Goerli or Set Hardhat Local Node
                        </h2>
                    )}
                </div>
            </Container>
        </div>
    )
}
