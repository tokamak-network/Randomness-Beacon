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
import { useMoralis, useWeb3Contract } from "react-moralis"
import { BackgroundImage } from "./BackgroundImage"
import { Button } from "./Button"
import { Container } from "./Container"
import { abi, contractAddresses as contractAddressesJSON } from "../../constants"
import { useNotification, Bell } from "web3uikit"
import { ethers } from "ethers"

export function Register({
    participatedRoundsLength,
    timeRemaining,
    registrationDurationForNextRound,
    startRegistrationTimeForNextRound,
    round,
    updateUI,
    isRegistrationOpen,
}: {
    participatedRoundsLength: string
    timeRemaining: string
    registrationDurationForNextRound: string
    startRegistrationTimeForNextRound: string
    round: string
    updateUI: () => Promise<void>
    isRegistrationOpen: boolean
}) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const contractAddresses: { [key: string]: string[] } = contractAddressesJSON
    const randomAirdropAddress =
        chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null
    const dispatch = useNotification()
    const {
        runContractFunction: registerForNextRound,
        isLoading,
        isFetching,
    } = useWeb3Contract({
        abi: abi,
        contractAddress: randomAirdropAddress!,
        functionName: "registerForNextRound",
        params: {},
    })
    async function registerFunction() {
        await registerForNextRound({
            onSuccess: handleSuccess,
            onError: (error: any) => {
                console.log(error)
                const iface = new ethers.utils.Interface(abi)
                let errorMessage = ""
                if (error?.data?.data?.data) {
                    errorMessage = iface.parseError(error?.data?.data?.data).name
                }
                dispatch({
                    type: "error",
                    message: error?.data?.data?.data
                        ? errorMessage
                        : error?.error?.message && error.error.message != "execution reverted"
                        ? error.error.message
                        : error?.data
                        ? error?.data?.message
                        : error?.message,
                    title: "Error Message",
                    position: "topR",
                    icon: <Bell />,
                })
            },
        })
        await updateUI()
    }
    const handleSuccess = async function (tx: any) {
        await tx.wait(1)
        handleNewNotification()
    }
    const handleNewNotification = function () {
        dispatch({
            type: "info",
            message: "Transaction Completed",
            title: "Tx Notification",
            position: "topR",
            icon: <Bell />,
        })
    }
    return (
        <div className="relative py-20 sm:pb-24 sm:pt-36">
            <BackgroundImage className="-bottom-14 -top-36 " />
            <Container className="relative pb-3.5">
                <div className="mx-auto max-w-2xl lg:max-w-4xl lg:px-12 ">
                    {randomAirdropAddress ? (
                        <>
                            {" "}
                            <h1 className="font-display text-5xl font-bold tracking-tighter text-blue-600 sm:text-7xl ">
                                Register For TON Airdrop
                            </h1>
                            {isRegistrationOpen ? (
                                <div className="mt-6 space-y-6 font-display text-2xl tracking-tight text-blue-900">
                                    <div>
                                        You are registering for round :{" "}
                                        <span className="font-semibold">{round}</span>
                                    </div>
                                </div>
                            ) : (
                                <div className="mt-6 space-y-6 font-display text-2xl tracking-tight text-red-900">
                                    Registration is closed
                                </div>
                            )}
                            <Button
                                className={
                                    "mt-10 w-full " + (isRegistrationOpen ? "" : "opacity-20")
                                }
                                disabled={isRegistrationOpen ? false : true}
                                onClick={registerFunction}
                            >
                                Register
                            </Button>
                            <dl className="mt-10 grid grid-cols-2 gap-x-10 gap-y-6 sm:mt-16 sm:gap-x-16 sm:gap-y-10 sm:text-center lg:auto-cols-auto lg:grid-flow-col lg:grid-cols-none lg:justify-start lg:text-left">
                                {[
                                    ["Registered", participatedRoundsLength],
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
                            Connect to Sepolia, Titan or Set Hardhat Local Node
                        </h2>
                    )}
                </div>
            </Container>
        </div>
    )
}
