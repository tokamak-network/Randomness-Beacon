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
import { abi, contractAddresses as contractAddressesJSON } from "../../constants"
import { useMoralis } from "react-moralis"
import { useNotification, Input, Table, Bell } from "web3uikit"
import { useState } from "react"
import { ethers } from "ethers"
import { Container } from "./Container"
// define type [Array(1), Array(1), addresses: Array(1), rankPoints: Array(1)]
interface Result {
    addresses: string[]
    rankPoints: string[]
}
export default function RankOfEachParticipantsMain({
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
    const contractAddresses: { [key: string]: string[] } = contractAddressesJSON
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
                abi: abi,
                contractAddress: randomAirdropAddress!,
                functionName: "getRankPointOfEachParticipants",
                params: {
                    _round: round,
                },
            }

            let result: Result = (await getRankPointOfEachParticipants({
                params: Options,
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
        <>
            <section id="speakers" aria-labelledby="speakers-title" className="py-20  sm:py-32">
                <Container>
                    {randomAirdropAddress ? (
                        <div className="mx-auto max-w-2xl lg:mx-0">
                            <h2
                                id="speakers-title"
                                className="font-display text-4xl font-medium tracking-tighter text-blue-600 sm:text-5xl"
                            >
                                Get Results
                            </h2>
                            <div className="mt-10 ml-1">
                                <Input
                                    label="Round"
                                    type="number"
                                    placeholder={currentRound}
                                    id="round"
                                    validation={{
                                        required: true,
                                        numberMax: Number(currentRound),
                                    }}
                                    onChange={(e) => setRound(e.target.value)}
                                    state={roundState}
                                    errorMessage="Round is required"
                                />
                            </div>
                            {participatedRounds?.length > 0 ? (
                                <div className="mt-6 ml-1 font-display text-xl tracking-tight text-blue-900">
                                    Rounds you've participated in :{" "}
                                    <span className="font-bold">
                                        {participatedRounds.toString()}
                                    </span>
                                </div>
                            ) : (
                                <div></div>
                            )}
                            <button
                                id="enterEventByCommit"
                                className="mt-7 inline-flex justify-center rounded-2xl bg-blue-600 p-4 text-base font-semibold text-white hover:bg-blue-500 focus:outline-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-500 active:text-white/70"
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
                        </div>
                    ) : (
                        <div></div>
                    )}

                    {tableContents.length > 0 ? (
                        <div className="mt-7">
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
                </Container>
            </section>
        </>
    )
}
