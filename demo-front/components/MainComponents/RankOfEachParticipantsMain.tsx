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
import { BigNumberish, ethers } from "ethers"
import { useState } from "react"
import { useMoralis, useWeb3Contract } from "react-moralis"
import { Bell, Input, Table, useNotification } from "web3uikit"
import {
    airdropConsumerAbi,
    consumerContractAddress as consumerContractAddressJSON,
} from "../../constants"
import { Container } from "./Container"
// define type [Array(1), Array(1), addresses: Array(1), rankPoints: Array(1)]
type Result = [
    [BigNumberish, BigNumberish, BigNumberish, BigNumberish],
    [string, string, string, string]
]
export default function RankOfEachParticipantsMain({
    round: currentRound = "0",
    participatedRounds,
    withdrawedRounds,
    updateUI,
}: {
    round: string
    participatedRounds: string[]
    withdrawedRounds: string[]
    updateUI: () => Promise<void>
}) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const [roundState, setRoundState] = useState<"initial" | "error" | "disabled" | "confirmed">(
        "initial"
    )
    const [round, setRound] = useState<string>("")
    const [isLoading, setIsLoading] = useState<boolean>(false)
    const contractAddresses: { [key: string]: string[] } = consumerContractAddressJSON
    const randomAirdropAddress =
        !isNaN(chainId) && chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null
    const dispatch = useNotification()
    const [tableContents, setTableContents] = useState<string[][]>([])
    // @ts-ignore
    const {
        runContractFunction: getPrizeAmountStartingAtFifthPlace,
        // @ts-ignore
    } = useWeb3Contract()

    const {
        runContractFunction: getWinnersIndexAndAddressAtRound,
        // @ts-ignore
    } = useWeb3Contract()
    // @ts-ignore
    const { runContractFunction: withdrawAirdropToken } = useWeb3Contract()
    function validation() {
        if (round == undefined || round == "") {
            setRoundState("error")
            return false
        }
        return true
    }
    async function withdrawAirdropTokenFunction() {
        if (validation()) {
            setIsLoading(true)
            const Options = {
                abi: airdropConsumerAbi,
                contractAddress: randomAirdropAddress!,
                functionName: "withdrawAirdropToken",
                params: {
                    round: round,
                },
            }
            await withdrawAirdropToken({
                params: Options,
                onSuccess: handleWithdrawAirdropTokenSuccess,
                onError: (error: any) => {
                    setIsLoading(false)
                    console.log(error)
                    const iface = new ethers.utils.Interface(airdropConsumerAbi)
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
            setIsLoading(false)
        }
    }
    const handleWithdrawAirdropTokenSuccess = async (tx: any) => {
        await tx.wait()
        setTimeout(() => {
            dispatch({
                type: "success",
                message: "Withdrawal Successful",
                title: "Success",
                position: "topR",
                icon: <Bell />,
            })
        }, 2000)
        await updateUI()
    }

    async function getWinnersIndexAndAddressAtRoundFunction() {
        if (validation()) {
            setIsLoading(true)
            const PrizeOptions = {
                abi: airdropConsumerAbi,
                contractAddress: randomAirdropAddress!,
                functionName: "getPrizeAmountStartingAtFifthPlace",
                params: {
                    round: round,
                },
            }

            const Options = {
                abi: airdropConsumerAbi,
                contractAddress: randomAirdropAddress!,
                functionName: "getWinnersIndexAndAddressAtRound",
                params: {
                    round: round,
                },
            }
            let result: Result = (await getWinnersIndexAndAddressAtRound({
                params: Options,
                onError: (error: any) => {
                    setIsLoading(false)
                    console.log(error)
                    const iface = new ethers.utils.Interface(airdropConsumerAbi)
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
            let prizeResult: BigNumberish = (await getPrizeAmountStartingAtFifthPlace({
                params: PrizeOptions,
                onError: (error: any) => {
                    setIsLoading(false)
                    console.log(error)
                    const iface = new ethers.utils.Interface(airdropConsumerAbi)
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
            })) as BigNumberish
            setIsLoading(false)
            getTableContents(result, prizeResult)
        }
    }
    const getTableContents = (result: Result, prizeResult: BigNumberish) => {
        let _results = []
        if (result[0][0].toString() == result[0][1].toString()) {
            dispatch({
                type: "error",
                message: "Random Number Not Generated Yet",
                title: "Error Message",
                position: "topR",
                icon: <Bell />,
            })
        }
        const prizeAmount: [string, string, string, string, string] = [
            "500",
            "77",
            "77",
            "77",
            ethers.utils.formatEther(prizeResult.toString()),
        ]
        if (result[0][0].toString() !== result[0][1].toString()) {
            for (let i = 0; i < 4; i++) {
                _results.push([result[1][i], prizeAmount[i]])
            }
            _results.push(["...rest of the participants", prizeAmount[4]])
        } else {
            for (let i = 0; i < 4; i++) {
                _results.push(["0x", prizeAmount[i]])
            }
            _results.push(["...rest of the participants", prizeAmount[4]])
        }

        for (let i = 0; i < 5; i++) {
            _results[i].unshift("#" + (i + 1))
        }
        // let mod = _results.length % 5
        // let len = _results.length
        // if (mod != 0) {
        //     for (let i = 0; i < 5 - mod; i++) {
        //         _results.push(["#" + (len + i + 1), "", ""])
        //     }
        // }
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
                                <div className="mt-6 ml-1 font-display text-xl tracking-tight text-blue-900">
                                    Rounds you've participated in :
                                </div>
                            )}
                            {withdrawedRounds?.length > 0 ? (
                                <div className="mt-1 ml-1 font-display text-xl tracking-tight text-blue-900">
                                    Rounds you've withdrawn :{" "}
                                    <span className="font-bold">
                                        {withdrawedRounds.toString()}
                                    </span>
                                </div>
                            ) : (
                                <div className="mt-1 ml-1 font-display text-xl tracking-tight text-blue-900">
                                    Rounds you've withdrawn :
                                </div>
                            )}
                            <button
                                id="enterEventByCommit"
                                className="mt-7 inline-flex justify-center rounded-2xl bg-blue-600 p-4 text-base font-semibold text-white hover:bg-blue-500 focus:outline-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-500 active:text-white/70"
                                disabled={isLoading}
                                type="button"
                                onClick={getWinnersIndexAndAddressAtRoundFunction}
                            >
                                <div>Get Ranking Results</div>
                            </button>
                            <button
                                id="enterEventByCommit"
                                className="ml-2 mt-7 inline-flex justify-center rounded-2xl bg-cyan-500 p-4 text-base font-semibold text-white hover:bg-cyan-600 focus:outline-none focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-cyan-500 active:text-white/70"
                                disabled={isLoading}
                                type="button"
                                onClick={withdrawAirdropTokenFunction}
                            >
                                {isLoading ? (
                                    <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                                ) : (
                                    <div>Withdraw</div>
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
                                header={["#Rank", "Address", "Prize Amount"]}
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
