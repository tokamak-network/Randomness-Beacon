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
import { useMoralis } from "react-moralis"
import { consumerContractAddress as consumerContractAddressJSON } from "../constants"
export default function Round({ round }: { round: string }) {
    const { chainId: chainIdHex, isWeb3Enabled } = useMoralis()
    const chainId = parseInt(chainIdHex!)
    const contractAddresses: { [key: string]: string[] } = consumerContractAddressJSON
    const randomAirdropAddress =
        chainId in contractAddresses
            ? contractAddresses[chainId][contractAddresses[chainId].length - 1]
            : null

    return (
        <div className="p-5">
            {randomAirdropAddress ? (
                <h2 className="pt-4 px-4 text-2xl subpixel-antialiased font-semibold">
                    Current Round: <span className="font-extrabold">{round}</span>
                </h2>
            ) : (
                <h2 className="py-4 px-4 font-bold text-2xl text-red-600">
                    Connect to Titan, Titan-Goerli or Set Hardhat Local Node
                </h2>
            )}
        </div>
    )
}

/**to reset an account, 
On metamask, go to settings/advanced/reset account */
