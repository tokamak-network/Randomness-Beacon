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
import { abi, contractAddresses } from "../constants"
import { useMoralis } from "react-moralis"
import { useEffect, useState } from "react"
import { createTestCases2 } from "../utils/testFunctions"
import { Input, useNotification, Form, Button } from "web3uikit"
import SetModal from "./SetModal"
import { ethers } from "ethers"
//import { useRouter } from "next/router"
import document from "global/document"

export default function SetUp({ updateUI, isSetUp }) {
    const [, updateState] = useState()
    //const router = useRouter()
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex)
    const raffleAddress = chainId in contractAddresses ? contractAddresses[chainId][0] : null
    const setUpParams = createTestCases2()[0]
    const dispatch = useNotification()

    const [formData, setFormData] = useState(undefined)

    const [editItem, setEditItem] = useState(false)
    const [modalInputValue, setModalInputValue] = useState("")
    const [isModalOpen, setIsModalOpen] = useState(false)
    const [nValue, setNValue] = useState(JSON.stringify(setUpParams.n))
    const [setUpProofs, setSetUpProofs] = useState(JSON.stringify(setUpParams.setupProofs))
    const [commitDuration, setCommitDuration] = useState()
    const [commitDurationState, setCommitDurationState] = useState("initial")
    const [revealDuration, setRevealDuration] = useState()
    const [revealDurationState, setRevealDurationState] = useState("initial")

    const { runContractFunction: setUp, isLoading, isFetching } = useWeb3Contract()
    function validation() {
        if (commitDuration == undefined || commitDuration == "" || commitDuration == 0) {
            setCommitDurationState("error")
            return false
        } else if (revealDuration == undefined || revealDuration == "" || revealDuration == 0) {
            setRevealDurationState("error")
            return false
        }
        return true
    }

    async function setUpFunction() {
        if (validation()) {
            const setUpOptions = {
                abi: abi,
                contractAddress: raffleAddress,
                functionName: "setUp",
                params: {
                    _commitDuration: parseInt(commitDuration),
                    _commitRevealDuration: parseInt(commitDuration) + parseInt(revealDuration),
                    _n: JSON.parse(nValue),
                    _proofs: JSON.parse(setUpProofs),
                },
            }

            await setUp({
                params: setUpOptions,
                onSuccess: handleSuccess,
                onError: (error) => {
                    dispatch({
                        type: "error",
                        message: error?.data?.message,
                        title: "Error Message",
                        position: "topR",
                        icon: "bell",
                    })
                    console.log(error)
                },
            })
            await updateUI()
        }
    }
    const handleSuccess = async function (tx) {
        await tx.wait(1)
        handleNewNotification(tx)
        //updateUI()
    }
    // function updateUI() {
    //     setFormData(undefined)
    // }
    const handleNewNotification = function () {
        dispatch({
            type: "info",
            message: "Transaction Completed",
            title: "Tx Notification",
            position: "topR",
            icon: "bell",
        })
    }

    const setValue = function (jsonString) {
        if (isModalOpen) {
            if (jsonString) {
                if (editItem === "n value") {
                    setNValue(jsonString)
                }
                if (editItem === "setupProofs") {
                    setSetUpProofs(jsonString)
                }
            }
            setIsModalOpen(false)
        }
    }
    const handleNValueEdit = function () {
        setEditItem("n value")
        setIsModalOpen(true)
    }
    const handleProofsEdit = function () {
        setEditItem("setupProofs")
        setIsModalOpen(true)
    }
    const onClose = function () {
        setIsModalOpen(false)
    }

    // useEffect(() => {
    //     if (isWeb3Enabled) {
    //     }
    // }, [isWeb3Enabled])

    return (
        <div className="p-5">
            <div className="border-dashed border-amber-950 border-2 rounded-lg p-10">
                <h3 data-testid="test-form-title" className="sc-eXBvqI eGDBJr">
                    Set Up
                </h3>
                <div className="mt-10">
                    <Input
                        label="Commit Duration in Seconds"
                        placeholder="120 (2 mins*)"
                        type="number"
                        id="CommitDuration"
                        validation={{ required: true, numberMin: 0 }}
                        value={commitDuration}
                        onChange={(e) => setCommitDuration(e.target.value)}
                        state={commitDurationState}
                    />
                </div>
                <div className="mt-10">
                    <Input
                        label="Reveal Duration in Seconds"
                        placeholder="120 (2 mins*)"
                        type="number"
                        id="RevealDuration"
                        validation={{ required: true, numberMin: 0 }}
                        value={revealDuration}
                        onChange={(e) => setRevealDuration(e.target.value)}
                        state={revealDurationState}
                    />
                </div>
                <div className="mt-9">
                    <Input
                        label="n value"
                        name="n value"
                        type="text"
                        width="100%"
                        value={nValue}
                        state="disabled"
                    />
                    <div className="mt-2">
                        <Button onClick={handleNValueEdit} text="Edit" theme="outline" />
                    </div>
                </div>
                <div className="mt-7">
                    <Input
                        label="setupProofs"
                        name="setupProofs"
                        type="text"
                        width="100%"
                        value={setUpProofs}
                        state="disabled"
                    />
                    <div className="mt-2">
                        <Button onClick={handleProofsEdit} text="Edit" theme="outline" />
                    </div>
                </div>
                <button
                    id="set-up"
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded ml-auto mt-7"
                    disabled={isLoading || isFetching}
                    type="button"
                    onClick={setUpFunction}
                >
                    {isLoading || isFetching ? (
                        <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                    ) : (
                        <div>SetUp</div>
                    )}
                </button>
            </div>
            <div>
                <SetModal
                    editItem={editItem}
                    isModalOpen={isModalOpen}
                    onClose={onClose}
                    setValue={setValue}
                    setModalInputValue={setModalInputValue}
                    modalInputValue={modalInputValue}
                />
            </div>
        </div>
    )
}
