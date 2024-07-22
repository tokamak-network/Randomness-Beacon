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
import { BigNumberish, ethers } from "ethers"
import { decodeError } from "ethers-decode-error"
import { useRef, useState } from "react"
import { useMoralis } from "react-moralis"
import { Bell, useNotification } from "web3uikit"
import {
    consumerContractAddress as consumerContractAddressJSON,
    crrngCoordinatorAbi,
    crrngCoordinatorAddress as crrngCoordinatorAddressJSON,
    randomDayAbi,
} from "../../constants"
import { BackgroundImage } from "./BackgroundImage"
import { Button } from "./Button"
import { Container } from "./Container"
declare type TValue = 1 | 2 | 3 | 4 | 5 | 6
declare type TDiceRef = {
    rollDice: (value: TValue) => void
}
export function Register({
    timeRemaining,
    registrationDurationForNextRound,
    startRegistrationTimeForNextRound,
    updateUI,
    isEventOpen,
    averageNumber,
}: {
    timeRemaining: string
    registrationDurationForNextRound: string
    startRegistrationTimeForNextRound: string
    updateUI: () => Promise<void>
    isEventOpen: boolean
    averageNumber: BigNumberish
}) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const [diceDataState, setDiceDataState] = useState<
        "error" | "initial" | "disabled" | "confirmed" | undefined
    >("initial")
    const [isFetching, setIsFetching] = useState<boolean>(false)
    const contractAddresses: { [key: string]: string[] } = consumerContractAddressJSON
    const randomAirdropAddress =
        !isNaN(chainId) && chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null
    const crrrngCoordinatorAddresses: { [key: string]: string[] } = crrngCoordinatorAddressJSON
    const getCrrngCoordinatorAddress =
        !isNaN(chainId) && chainId in crrrngCoordinatorAddresses
            ? crrrngCoordinatorAddresses[chainId][crrrngCoordinatorAddresses[chainId].length - 1]
            : null
    const dispatch = useNotification()

    async function registerFunction() {
        setIsFetching(true)
        const provider = new ethers.providers.Web3Provider((window as any).ethereum, "any")
        // Prompt user for account connections
        await provider.send("eth_requestAccounts", [])
        const signer = provider.getSigner()
        const randomAirdropContract = new ethers.Contract(
            randomAirdropAddress!,
            randomDayAbi,
            provider
        )

        const crrrngCoordinator = new ethers.Contract(
            getCrrngCoordinatorAddress!,
            crrngCoordinatorAbi,
            provider
        )
        try {
            const feeData = await provider.getFeeData()
            let gasPrice = feeData.maxFeePerGas
            if (gasPrice == null) gasPrice = feeData.gasPrice
            const directFundingCost = await crrrngCoordinator.estimateDirectFundingPrice(
                210000,
                gasPrice?.toString()
            )

            const directFundingCostInt = Math.floor(Number(directFundingCost.toString()))
            const tx = await randomAirdropContract
                .connect(signer)
                .requestRandomWord({ gasLimit: 318111, value: directFundingCostInt })
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
        <div className="relative py-20 sm:pb-24 sm:pt-36 mb-16">
            <BackgroundImage className="-bottom-14 -top-36 " />
            <Container className="relative pb-3.5">
                <div className="mx-auto max-w-2xl lg:max-w-4xl lg:px-12">
                    {randomAirdropAddress ? (
                        <>
                            {" "}
                            <h1 className="font-display text-5xl font-bold tracking-tighter text-blue-600 sm:text-7xl ">
                                Crypto Target 700 🎯
                            </h1>
                            {isEventOpen ? (
                                <div className="mt-6 space-y-6 font-display text-2xl tracking-tight text-blue-900">
                                    <div>
                                        Your current average number is{": "}
                                        <span className="font-bold text-4xl">
                                            {" "}
                                            {averageNumber.toString()}
                                        </span>
                                    </div>
                                </div>
                            ) : (
                                <div className="mt-6 space-y-6 font-display text-2xl tracking-tight text-red-900">
                                    The event is Not in progress.
                                </div>
                            )}
                            <div className="mt-2 flex" style={{ alignItems: "center" }}>
                                <div className="flex-1 mb-11">
                                    <Button
                                        className={
                                            "mt-10 w-full " + (!isEventOpen ? "opacity-20" : "")
                                        }
                                        disabled={!isEventOpen || isFetching ? true : false}
                                        onClick={registerFunction}
                                    >
                                        {isFetching ? (
                                            <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                                        ) : (
                                            <div>{"Request RandomWord"}</div>
                                        )}
                                    </Button>
                                </div>
                            </div>
                            {/* <div className="mt-6 space-y-6 font-display text-2xl tracking-tight text-blue-900">
                                <div>RequestIds: {requestIds.toString()}</div>
                                <div>RandomNumbers: {randomNums.toString()}</div>
                            </div> */}
                            <dl className="mt-10 grid grid-cols-2 gap-x-10 gap-y-6 sm:mt-16 sm:gap-x-16 sm:gap-y-10 sm:text-center lg:auto-cols-auto lg:grid-flow-col lg:grid-cols-none lg:justify-start lg:text-left">
                                {[
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
                            Connect to Titan-Sepolia, Titan
                        </h2>
                    )}
                </div>
            </Container>
        </div>
    )
}
