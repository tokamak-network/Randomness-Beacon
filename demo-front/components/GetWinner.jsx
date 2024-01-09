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
import { useState } from "react"
import { createTestCases2 } from "./../utils/testFunctions"
import { Input, useNotification } from "web3uikit"
import Withdraw from "./Withdraw"
import RankOfEachParticipants from "./RankOfEachParticipants"
export default function GetWinner({ round: currentRound, participatedRounds }) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex)
    const randomAirdropAddress =
        chainId in contractAddresses ? contractAddresses[chainId][0] : null
    const setUpParams = createTestCases2()[0]
    const dispatch = useNotification()
    const { runContractFunction: getWinnerAddress, isLoading, isFetching } = useWeb3Contract()
    const [roundState, setRoundState] = useState("initial")
    let [winnerAddress, setWinnerAddress] = useState("0x")
    const [round, setRound] = useState(undefined)
    function validation() {
        if (round == undefined || round == "") {
            setRoundState("error")
            return false
        }
        return true
    }
    async function getWinnerFunction() {
        if (validation()) {
            const setUpOpions = {
                abi: abi,
                contractAddress: randomAirdropAddress,
                functionName: "getWinnerAddress",
                params: {
                    _round: parseInt(round),
                },
            }

            winnerAddress = await getWinnerAddress({
                params: setUpOpions,
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
            setWinnerAddress(winnerAddress)
        }
    }
    return (
        <div className="p-5">
            <div className="border-dashed border-amber-950 border-2 rounded-lg p-10">
                <h3 data-testid="test-form-title" className="sc-eXBvqI eGDBJr">
                    Get Result
                </h3>
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
                    <div className="mt-1">
                        Rounds you've participated in : {participatedRounds.toString()}
                    </div>
                </div>

                <button
                    id="enterEventByCommit"
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded ml-auto mt-7"
                    disabled={isLoading || isFetching}
                    type="button"
                    onClick={getWinnerFunction}
                >
                    {isLoading || isFetching ? (
                        <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                    ) : (
                        <div>Get Winner Address</div>
                    )}
                </button>
                <div className="mt-5">
                    Winnder Address at Round {round} : {winnerAddress}
                </div>
                <div>
                    <Withdraw round={round} />
                </div>
            </div>
        </div>
    )
}
