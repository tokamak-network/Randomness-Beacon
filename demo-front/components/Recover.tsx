// Copyright 2023 justin
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
import { createTestCases2 } from "../utils/testFunctions"
import { Input, useNotification, Button, Bell } from "web3uikit"
import SetModal from "./SetModal"
import { ethers } from "ethers"

export default function Recover({ round: currentRound }: { round: string }) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const [roundState, setRoundState] = useState<"error" | "initial" | "confirmed" | "disabled">(
        "initial"
    )
    const [round, setRound] = useState<string>("")
    const chainId = parseInt(chainIdHex!)
    const contractAddresses: { [key: string]: string[] } = contractAddressesJSON
    const randomAirdropAddress =
        chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null
    const recoverParams = createTestCases2()[0]
    const dispatch = useNotification()
    // @ts-ignore
    const { runContractFunction: recover, isLoading, isFetching } = useWeb3Contract()
    const [editItem, setEditItem] = useState<string>("")
    const [modalInputValue, setModalInputValue] = useState("")
    const [isModalOpen, setIsModalOpen] = useState(false)
    const [recoveryProofs, setRecoveryProofs] = useState(
        JSON.stringify(recoverParams.recoveryProofs)
    )
    function validation() {
        if (round == undefined || round == "") {
            setRoundState("error")
            return false
        }
        return true
    }
    async function recoverFunction() {
        // const provider = new ethers.providers.Web3Provider((window as any).ethereum, "any");
        // await provider.send("eth_requestAccounts", []);
        // const signer = provider.getSigner();
        // const randomAirdropContract = new ethers.Contract(randomAirdropAddress!, abi, provider);
        //const estimateGas = await randomAirdropContract.connect(signer).estimateGas.recover(parseInt(round), JSON.parse(recoveryProofs))
        // const tx = await randomAirdropContract.connect(signer).recover(parseInt(round), JSON.parse(recoveryProofs), {gasLimit:3000000})
        // console.log(await tx.wait())

        if (validation()) {
            const recoveryOptions = {
                abi: abi,
                contractAddress: randomAirdropAddress!,
                functionName: "recover",
                params: {
                    _round: parseInt(round),
                    proofs: JSON.parse(recoveryProofs),
                },
            }

            await recover({
                params: recoveryOptions,
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
        }
    }
    const handleSuccess = async function (tx: any) {
        await tx.wait(1)
        handleNewNotification()

        //updateUI()
    }
    //async function updateUI() {}
    const handleNewNotification = function () {
        dispatch({
            type: "info",
            message: "Transaction Completed",
            title: "Tx Notification",
            position: "topR",
            icon: <Bell />, //"bell",
        })
    }

    const handleProofsEdit = function () {
        setEditItem("recoveryProofs")
        setIsModalOpen(true)
    }
    const onClose = function () {
        setIsModalOpen(false)
    }
    const setValue = function (jsonString: string) {
        if (isModalOpen) {
            if (jsonString) {
                if (editItem === "recoveryProofs") {
                    setRecoveryProofs(jsonString)
                }
            }
            setIsModalOpen(false)
        }
    }

    return (
        <div className="p-5 mb-5">
            <div className="border-dashed border-amber-950 border-2 rounded-lg p-10">
                <SetModal
                    editItem={editItem}
                    isModalOpen={isModalOpen}
                    onClose={onClose}
                    setValue={setValue}
                    setModalInputValue={setModalInputValue}
                    modalInputValue={modalInputValue}
                    key={editItem}
                />
                <h3 data-testid="test-form-title" className="sc-eXBvqI eGDBJr">
                    Recover
                </h3>
                <div className="mb-2 mt-5">
                    <Input
                        label="Round"
                        type="number"
                        placeholder={currentRound}
                        id="round"
                        validation={{ required: true, numberMax: Number(currentRound) }}
                        onChange={(e) => setRound(e.target.value)}
                        state={roundState}
                        errorMessage="Round is required"
                    />
                </div>
                <div className="mt-7">
                    <Input
                        label="recoveryProofs"
                        name="recoveryProofs"
                        type="text"
                        width="100%"
                        value={recoveryProofs}
                        state="disabled"
                    />
                    <div className="mt-2">
                        <Button onClick={handleProofsEdit} text="Edit" theme="outline" />
                    </div>
                </div>
                <button
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded ml-auto mt-5"
                    disabled={isLoading || isFetching}
                    type="submit"
                    onClick={recoverFunction}
                >
                    {isLoading || isFetching ? (
                        <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                    ) : (
                        <div>Recover</div>
                    )}
                </button>
                {/* <div>
                <ProgressBar total={10000} value={2200} />
            </div> */}
            </div>
        </div>
    )
}

/**to reset an account, 
On metamask, go to settings/advanced/reset account */
