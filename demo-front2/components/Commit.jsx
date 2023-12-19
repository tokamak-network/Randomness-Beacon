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
import { Input, useNotification } from "web3uikit"
import { getBitLenth2, getLength } from "../utils/testFunctions"
import { toBeHex, dataLength } from "ethers"
import React from "react"
const ReactJson = dynamic(() => import("react-json-view-with-toggle"), {
    ssr: false,
})
export default function Commit({ commitIndex, entranceFee }) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex)
    const raffleAddress = chainId in contractAddresses ? contractAddresses[chainId][0] : null
    let [round, setRound] = useState(0)
    const [commitCalldata, setCommitCalldata] = useState()
    const setUpParams = createTestCases2()[0]
    const [commitData, setCommitData] = useState()
    const [commitDataState, setCommitDataState] = useState("initial")
    const { runContractFunction: enterRafByCommit, isLoading, isFetching } = useWeb3Contract()
    const dispatch = useNotification()
    async function enterRafByCommitFunction(data) {
        const enterRafByCommitOptions = {
            abi: abi,
            contractAddress: raffleAddress,
            functionName: "enterRafByCommit",
            params: {
                _c: commitCalldata,
            },
            msgValue: entranceFee,
        }
        await enterRafByCommit({
            params: enterRafByCommitOptions,
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
            <h3 data-testid="test-form-title" className="sc-eXBvqI eGDBJr">
                Enter Raffle by Commit
            </h3>
            <div className="my-2">
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
                    errorMessage="Entrance Fee is required"
                    width="50%"
                />
            </div>
            <div className="mt-7 ml-1 text-lg">
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
            {/* <Form
                id="set-up"
                title="Enter Raffle By Commit"
                onSubmit={enterRafByCommitFunction}
                isDisabled={isLoading || isFetching}
                buttonConfig={{
                    text: "Set Up",
                    size: "large",
                    type: "button",
                    onClick: function noRefCheck() {},
                    disabled: isLoading || isFetching,
                    isLoading: isLoading || isFetching,
                    loadingProps: {
                        spinnerType: "loader",
                        spinnerColor: "black",
                    },
                    loadingText: "Setting Up",
                }}
                customFooter={
                    <button
                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded ml-auto"
                        disabled={isLoading || isFetching}
                        type="submit"
                    >
                        {isLoading || isFetching ? (
                            <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                        ) : (
                            <div>Commit</div>
                        )}
                    </button>
                }
                data={[
                    {
                        id: "Commit Value",
                        inputWidth: "100%",
                        name: "n value",
                        type: "box",
                        value: (
                            <Input
                                label="n value"
                                name="n value"
                                type="text"
                                width="100%"
                                value={JSON.stringify(
                                    setUpParams.commitList[parseInt(commitIndex)]
                                )}
                                state="disabled"
                            />
                        ),
                    },
                ]}
            /> */}
        </div>
    )
}
