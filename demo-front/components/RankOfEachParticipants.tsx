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
import { ethers } from "ethers"
import { useState } from "react"
import { useMoralis, useWeb3Contract } from "react-moralis"
import { Bell, Input, Table, useNotification } from "web3uikit"
import {
    consumerContractAddress as consumerContractAddressJSON,
    cryptoDiceConsumerAbi,
} from "../constants"
// define type [Array(1), Array(1), addresses: Array(1), rankPoints: Array(1)]
interface Result {
    addresses: string[]
    rankPoints: string[]
}
export default function RankOfEachParticipants({
    round: currentRound = "0",
    participatedRounds,
}: {
    round: string
    participatedRounds: string[]
}) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const [roundState, setRoundState] = useState<"initial" | "error" | "disabled" | "confirmed">(
        "initial"
    )
    const [round, setRound] = useState<string>("")
    const contractAddresses: { [key: string]: string[] } = consumerContractAddressJSON
    const randomAirdropAddress =
        chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null
    const dispatch = useNotification()
    const [tableContents, setTableContents] = useState<string[][]>([])

    const {
        runContractFunction: getRankPointOfEachParticipants,
        isLoading,
        isFetching, // @ts-ignore
    } = useWeb3Contract()
    function validation() {
        if (round == undefined || round == "") {
            setRoundState("error")
            return false
        }
        return true
    }
    async function getRankPointOfEachParticipantsFunction() {
        if (validation()) {
            const Options = {
                abi: cryptoDiceConsumerAbi,
                contractAddress: randomAirdropAddress!,
                functionName: "getRankPointOfEachParticipants",
                params: {
                    round: round,
                },
            }

            let result: Result = (await getRankPointOfEachParticipants({
                params: Options,
                onError: (error: any) => {
                    console.log(error)
                    const iface = new ethers.utils.Interface(cryptoDiceConsumerAbi)
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
            })) as Result
            getTableContents(result)
        }
    }
    const getTableContents = (result: Result) => {
        let _results = []
        if (result) {
            for (let i = 0; i < result.addresses.length; i++) {
                _results.push([result.addresses[i], BigInt(result.rankPoints[i]).toString()])
            }
        }
        _results.sort((a, b) => {
            return BigInt(a[1]) < BigInt(b[1]) ? 1 : BigInt(b[1]) < BigInt(a[1]) ? -1 : 0
        })
        for (let i = 0; i < _results.length; i++) {
            _results[i].unshift("#" + (i + 1))
        }
        let mod = _results.length % 5
        let len = _results.length
        if (mod != 0) {
            for (let i = 0; i < 5 - mod; i++) {
                _results.push(["#" + (len + i + 1), "", ""])
            }
        }
        setTableContents(_results)
    }
    return (
        <div className="p-5">
            <div className="border-dashed border-slate-300 border-2 rounded-lg p-10">
                <div className="mb-2 font-bold">Get Results</div>
                <div className="mt-5">
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
                {participatedRounds?.length > 0 ? (
                    <div className="mt-4">
                        Rounds you've participated in :{" "}
                        <span className="font-bold">{participatedRounds.toString()}</span>
                    </div>
                ) : (
                    <div></div>
                )}

                <button
                    id="enterEventByCommit"
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded ml-auto mt-7"
                    disabled={isLoading || isFetching}
                    type="button"
                    onClick={getRankPointOfEachParticipantsFunction}
                >
                    {isLoading || isFetching ? (
                        <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                    ) : (
                        <div>Get Rank Point For All Participants</div>
                    )}
                </button>
                {tableContents.length > 0 ? (
                    <div className="mt-5">
                        <Table
                            columnsConfig="80px 450px 450px 450px 80px"
                            data={tableContents}
                            header={["#Rank", "Address", "Rank Point"]}
                            maxPages={5}
                            onPageNumberChanged={function noRefCheck() {}}
                            onRowClick={function noRefCheck() {}}
                            pageSize={5}
                        />
                    </div>
                ) : (
                    <div></div>
                )}
            </div>
        </div>
    )
}
