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
import { abi, contractAddresses } from "./../constants"
import { useMoralis } from "react-moralis"
import { useNotification, Input, Table, Avatar, Tag } from "web3uikit"
import { useState } from "react"
export default function RankOfEachParticipants({ round: currentRound, participatedRounds }) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex)
    const [roundState, setRoundState] = useState("initial")
    const [round, setRound] = useState(undefined)
    const randomAirdropAddress =
        chainId in contractAddresses ? contractAddresses[chainId][0] : null
    const dispatch = useNotification()
    const [RankOfEachParticipants, setRankOfEachParticipants] = useState(undefined)
    const [tableContents, setTableContents] = useState([])
    const {
        runContractFunction: getRankPointOfEachParticipants,
        isLoading,
        isFetching,
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
                abi: abi,
                contractAddress: randomAirdropAddress,
                functionName: "getRankPointOfEachParticipants",
                params: {
                    _round: round,
                },
            }

            let result = await getRankPointOfEachParticipants({
                params: Options,
                onError: (error) => {
                    dispatch({
                        type: "error",
                        message: error?.error?.message
                            ? error.error.message
                            : error?.data?.message,
                        title: "Error Message",
                        position: "topR",
                        icon: "bell",
                    })
                },
            })
            setRankOfEachParticipants(result)
            getTableContents(result)
        }
    }
    const getTableContents = (result) => {
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
            <div className="border-dashed border-amber-950 border-2 rounded-lg p-10">
                <div className="mb-2 font-bold">Get Results</div>
                <div className="mt-5">
                    <Input
                        label="Round"
                        type="number"
                        placeholder={currentRound}
                        id="round"
                        validation={{ required: true, numberMax: currentRound }}
                        onChange={(e) => setRound(e.target.value)}
                        state={roundState}
                        errorMessage="Round is required"
                    />
                </div>
                {participatedRounds?.length > 0 ? (
                    <div className="mt-1">
                        Rounds you've participated in : {participatedRounds.toString()}
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
