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
import { useWeb3Contract } from "react-moralis"
import { abi, contractAddresses as contractAddressesJSON } from "../constants"
import { useMoralis } from "react-moralis"
import { useState } from "react"
import { Input, useNotification, Bell } from "web3uikit"
import { ethers } from "ethers"

export default function StartRegistration({ updateUI }: { updateUI: () => Promise<void> }) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const contractAddresses: { [key: string]: string[] } = contractAddressesJSON
    const randomAirdropAddress =
        chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null
    const dispatch = useNotification()

    const [registrationDuration, setRegistrationDuration] = useState<string>("")
    const [registrationDurationState, setRegistrationDurationState] = useState<
        "initial" | "error" | "disabled" | "confirmed"
    >("initial")
    const [isFetching, setIsFetching] = useState<boolean>(false)
    // @ts-ignore
    const { runContractFunction: startRegistration, isLoading } = useWeb3Contract()

    function validation() {
        if (
            registrationDuration == undefined ||
            registrationDuration == "" ||
            registrationDuration == "0"
        ) {
            setRegistrationDurationState("error")
            return false
        }
        return true
    }
    async function startRegistrationFunction() {
        if (validation()) {
            const startRegistrationOptions = {
                abi: abi,
                contractAddress: randomAirdropAddress!,
                functionName: "startRegistration",
                params: {
                    _registrationDuration: parseInt(registrationDuration),
                },
            }

            // const provider = new ethers.providers.Web3Provider((window as any).ethereum, "any")
            // // Prompt user for account connections
            // await provider.send("eth_requestAccounts", [])
            // const signer = provider.getSigner()
            // const randomAirdropContract = new ethers.Contract(randomAirdropAddress!, abi, provider)
            // try {
            //     // await randomAirdropContract
            //     //     .connect(signer)
            //     //     .startRegistration(parseInt(registrationDuration), { gasLimit: 300000 })
            //     const estimageGas = await randomAirdropContract.estimateGas.startRegistration(
            //         parseInt(registrationDuration)
            //     )
            //     console.log(parseInt(estimageGas.toString()))
            // } catch (error) {
            //     console.log(error)
            // }

            await startRegistration({
                params: startRegistrationOptions,
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
                    setRegistrationDurationState("initial")
                    setIsFetching(false)
                },
                onSuccess: handleSuccess,
            })
            await updateUI()
        }
    }
    const handleSuccess = async (tx: any) => {
        await tx.wait(1)
        setRegistrationDurationState("confirmed")
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
                className="border-dashed border-amber-950 border-2 rounded-lg p-10"
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
                <button
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded ml-auto mt-7"
                    disabled={isLoading || isFetching}
                    type="button"
                    onClick={startRegistrationFunction}
                >
                    {isLoading || isFetching ? (
                        <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                    ) : (
                        <div>Start Registration</div>
                    )}
                </button>
            </div>
        </div>
    )
}
