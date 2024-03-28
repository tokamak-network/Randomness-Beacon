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
import { BigNumber, ethers } from "ethers"
import { decodeError } from "ethers-decode-error"
import { useState } from "react"
import { useMoralis, useWeb3Contract } from "react-moralis"
import { Bell, Input, useNotification } from "web3uikit"
import {
    consumerContractAddress as consumerContractAddressJSON,
    cryptoDiceConsumerAbi,
} from "../constants"
//import titanSDK from "@tokamak-network/titan-sdk"

export default function StartRegistration({ updateUI }: { updateUI: () => Promise<void> }) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const contractAddresses: { [key: string]: string[] } = consumerContractAddressJSON
    const randomAirdropAddress =
        chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null
    const dispatch = useNotification()

    const [registrationDuration, setRegistrationDuration] = useState<string>("")
    const [totalPrizeAmount, setTotalPrizeAmount] = useState<string>("")
    const [totalPrizeAmountState, setTotalPrizeAmountState] = useState<
        "initial" | "error" | "disabled" | "confirmed"
    >("initial")
    const [registrationDurationState, setRegistrationDurationState] = useState<
        "initial" | "error" | "disabled" | "confirmed"
    >("initial")
    const [isFetching, setIsFetching] = useState<boolean>(false)
    // @ts-ignore
    const { runContractFunction: startRegistration } = useWeb3Contract()

    function validation() {
        if (
            registrationDuration == undefined ||
            registrationDuration == "" ||
            registrationDuration == "0" ||
            totalPrizeAmount == undefined ||
            totalPrizeAmount == "" ||
            totalPrizeAmount == "0"
        ) {
            setRegistrationDurationState("error")
            setTotalPrizeAmountState("error")
            return false
        }
        return true
    }
    async function startRegistrationFunction() {
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
                    .startRegistration(
                        parseInt(registrationDuration),
                        BigNumber.from(totalPrizeAmount).mul(
                            BigNumber.from("1000000000000000000")
                        ),
                        { gasLimit: 150000 }
                    )
                await handleSuccess(tx)
            } catch (error: any) {
                console.log(error)
                const decodedError = decodeError(decodeError(error))
                dispatch({
                    type: "error",
                    message: decodedError.error,
                    title: "Error Message",
                    position: "topR",
                    icon: <Bell />,
                })
                setRegistrationDurationState("initial")
                setTotalPrizeAmountState("initial")
                setIsFetching(false)
            }
            await updateUI()
        }
    }
    const handleSuccess = async (tx: any) => {
        await tx.wait()
        setRegistrationDurationState("confirmed")
        setTotalPrizeAmountState("confirmed")
        setIsFetching(false)
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
        <div className="p-5">
            <div
                className="border-dashed border-slate-300 border-2 rounded-lg p-10"
                key="bordercontainer"
            >
                <h3 data-testid="test-form-title" className="sc-eXBvqI eGDBJr" key="h3">
                    Start Registration
                </h3>
                <div className="mt-10">
                    <Input
                        label="Registration Duration in Seconds"
                        placeholder="120 (2 mins*)"
                        type="number"
                        id="RegistrationDuration"
                        validation={{ required: true, numberMin: 0 }}
                        value={registrationDuration}
                        onChange={(e) => setRegistrationDuration(e.target.value)}
                        state={registrationDurationState}
                    />
                </div>
                <div className="mt-10">
                    <Input
                        label="total prize amount"
                        placeholder="1000 (=1000 * 1e18)"
                        type="number"
                        id="TotalPrizeAmount"
                        validation={{ required: true, numberMin: 0 }}
                        value={totalPrizeAmount}
                        onChange={(e) => setTotalPrizeAmount(e.target.value)}
                        state={totalPrizeAmountState}
                    />
                </div>
                <button
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded ml-auto mt-7"
                    disabled={isFetching}
                    type="button"
                    onClick={startRegistrationFunction}
                >
                    {isFetching ? (
                        <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                    ) : (
                        <div>Start Registration</div>
                    )}
                </button>
            </div>
        </div>
    )
}
