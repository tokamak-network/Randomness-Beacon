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
import { useNotification, Input } from "web3uikit"
import { useState } from "react"
export default function RankOfEachParticipants({ round: currentRound }) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex)
    const [roundState, setRoundState] = useState("initial")
    const [round, setRound] = useState(undefined)
    const raffleAddress = chainId in contractAddresses ? contractAddresses[chainId][0] : null
    const dispatch = useNotification()
    const [RankOfEachParticipants, setRankOfEachParticipants] = useState(undefined)
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
                contractAddress: raffleAddress,
                functionName: "getRankPointOfEachParticipants",
                params: {
                    _round: round,
                },
            }

            let result = await getRankPointOfEachParticipants({
                params: Options,
                onError: (error) => {
                    console.log(error)
                    dispatch({
                        type: "error",
                        message: error?.data?.message,
                        title: "Error Message",
                        position: "topR",
                        icon: "bell",
                    })
                },
            })
            setRankOfEachParticipants(result)
            console.log(RankOfEachParticipants)
        }
    }
    return (
        <div className="p-5">
            <div className="border-dashed border-amber-950 border-2 rounded-lg p-10">
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

                <button
                    id="enterRaffleByCommit"
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded ml-auto mt-7"
                    disabled={isLoading || isFetching}
                    type="button"
                    onClick={getRankPointOfEachParticipantsFunction}
                >
                    {isLoading || isFetching ? (
                        <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                    ) : (
                        <div>Get RankPoint Of Each Participants</div>
                    )}
                </button>
                {RankOfEachParticipants ? (
                    <div>
                        <div>{RankOfEachParticipants.addresses.toString()}</div>
                        <div>{RankOfEachParticipants.rankPoints.toString()}</div>
                    </div>
                ) : (
                    <div></div>
                )}
            </div>
        </div>
    )
}
