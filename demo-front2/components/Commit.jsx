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
import dynamic from "next/dynamic"
import { abi, contractAddresses } from "./../constants"
import { useMoralis } from "react-moralis"
import { useEffect, useState } from "react"
import { createTestCases2 } from "./../utils/testFunctions"
import { Input, useNotification, Button } from "web3uikit"
import { getBitLenth2, getLength } from "../utils/testFunctions"
import { toBeHex, dataLength, ethers } from "ethers"
import React from "react"
const ReactJson = dynamic(() => import("react-json-view-with-toggle"), {
    ssr: false,
})
export default function Commit() {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex)
    const raffleAddress = chainId in contractAddresses ? contractAddresses[chainId][0] : null
    const [commitCalldata, setCommitCalldata] = useState()
    const [commitData, setCommitData] = useState()
    const [commitDataState, setCommitDataState] = useState("initial")
    const { runContractFunction: enterRafByCommit, isLoading, isFetching } = useWeb3Contract()
    const dispatch = useNotification()
    function validation() {
        if (commitData == undefined || commitData == "") {
            setCommitDataState("error")
            return false
        } else if (commitData == "0x" || commitData == "0" || commitData == 0) {
            dispatch({
                type: "error",
                message: "Commit Value cannot be 0",
                title: "Error Message",
                position: "topR",
                icon: "bell",
            })
            return false
        }
        return true
    }
    async function enterRafByCommitFunction() {
        if (validation()) {
            const enterRafByCommitOptions = {
                abi: abi,
                contractAddress: raffleAddress,
                functionName: "enterRafByCommit",
                params: {
                    _c: commitCalldata,
                },
            }
            await enterRafByCommit({
                params: enterRafByCommitOptions,
                onSuccess: handleSuccess,
                onError: (error) => {
                    dispatch({
                        type: "error",
                        message:
                            error?.error?.message && error.error.message != "execution reverted"
                                ? error.error.message
                                : new ethers.Interface(abi).parseError(
                                      error.error.data.originalError.data
                                  ).name,
                        title: "Error Message",
                        position: "topR",
                        icon: "bell",
                    })
                    console.log(error)
                },
            })
        }
    }
    const handleSuccess = async function (tx) {
        await tx.wait(1)
        handleNewNotification(tx)
        //updateUI()
    }
    //async function updateUI() {}
    const handleNewNotification = function () {
        dispatch({
            type: "info",
            message: "Transaction Completed",
            title: "Tx Notification",
            position: "topR",
            icon: "bell",
        })
    }
    useEffect(() => {
        if (isWeb3Enabled) {
            //updateUI()
        }
    }, [isWeb3Enabled])
    return (
        <div className="border-dashed border-amber-950 border-2 rounded-lg p-10 m-5">
            <h3 data-testid="test-form-title" className="sc-eXBvqI eGDBJr font-bold">
                Join Christmas Event by Commit
            </h3>
            <div className="mb-2 mt-5 flex flex-row">
                <Input
                    label="Commit Value in Decimal"
                    type="text"
                    placeholder=""
                    id="CommitValue"
                    validation={{ required: true }}
                    value={commitData}
                    onChange={(e) => {
                        setCommitData(e.target.value)
                        let stringVal = e.target.value
                        if (e.target.value.length == 0) stringVal = "0"
                        setCommitCalldata({
                            val: toBeHex(stringVal, getLength(dataLength(toBeHex(stringVal)))),
                            bitlen: getBitLenth2(BigInt(stringVal)),
                        })
                    }}
                    state={commitDataState}
                    errorMessage="Commit Value is required"
                    width="50%"
                />
                <Button
                    style={{ marginLeft: "10px", fontWeight: "bold" }}
                    onClick={() => {
                        let rand = window.crypto.getRandomValues(new Uint8Array(2048 / 8))
                        const bytesHex = rand.reduce(
                            (o, v) => o + ("00" + v.toString(16)).slice(-2),
                            ""
                        )
                        setCommitData(BigInt("0x" + bytesHex).toString(10))
                        let stringVal = BigInt("0x" + bytesHex).toString(10)
                        if (stringVal.length == 0) stringVal = "0"
                        setCommitCalldata({
                            val: toBeHex(stringVal, getLength(dataLength(toBeHex(stringVal)))),
                            bitlen: getBitLenth2(BigInt(stringVal)),
                        })
                    }}
                    text="Auto Generate"
                    theme="primary"
                />
            </div>
            <div
                className="mt-7 ml-1 text-base"
                style={{ textOverflow: "ellipsis", overflow: "hidden" }}
            >
                {/* calldata: {JSON.stringify(commitCalldata)} */}
                <ReactJson src={commitCalldata} />
            </div>
            <button
                id="enterRaffleByCommit"
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded ml-auto mt-7"
                disabled={isLoading || isFetching}
                type="button"
                onClick={enterRafByCommitFunction}
            >
                {isLoading || isFetching ? (
                    <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                ) : (
                    <div>Commit</div>
                )}
            </button>
            <div className="mt-2">
                <div>
                    Commit your value using the Auto Generate button or Type your number manually.
                </div>
                <div>*Auto Generate button uses the window.crypto.getRandomValues function.</div>
            </div>
        </div>
    )
}
