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
import { useNotification } from "web3uikit"
export default function Withdraw({ round }) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex)
    const randomAirdropAddress =
        chainId in contractAddresses ? contractAddresses[chainId][0] : null
    const dispatch = useNotification()
    const { runContractFunction: withdraw, isLoading, isFetching } = useWeb3Contract()
    async function withdrawFunction() {
        const withdrawOpions = {
            abi: abi,
            contractAddress: randomAirdropAddress,
            functionName: "withdraw",
            params: {
                _round: round,
            },
        }

        await withdraw({
            params: withdrawOpions,
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
    }
    return (
        <div>
            <button
                id="enterEventByCommit"
                className="bg-teal-400 hover:bg-teal-600 text-white font-bold py-3 px-4 rounded ml-auto mt-7"
                disabled={isLoading || isFetching}
                type="button"
                onClick={withdrawFunction}
            >
                {isLoading || isFetching ? (
                    <div className="animate-spin spinner-border h-8 w-8 border-b-2 rounded-full"></div>
                ) : (
                    <div>Withdraw</div>
                )}
            </button>
            <span className="ml-2">*only winner can withdraw</span>
        </div>
    )
}
