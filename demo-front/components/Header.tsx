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
import { ConnectButton } from "web3uikit"
import Link from "next/link"
import Image from "next/image"
const imageLoader = ({ src, width, quality }:any) => {
    return `../tokamaklogo.png`
}

export default function Header() {
    return (
        <div className="shadow-sm shadow-cyan-500/50 bg-slate-100 p-5 pl-10 border-b-2 flex flex-row justify-between items-center font-semibold">
            <Link href="/" key="5">
                <a className="flex flex-row items-center">
                    <Image
                        src="../tokamaklogo.png"
                        loader={imageLoader}
                        width={45}
                        height={35}
                        alt="Picture of the author"
                    />
                    <h1 className="py-4 px-4 font-bold text-3xl">TON Random Airdrop</h1>
                </a>
            </Link>

            <div className="flex flex-row items-center">
                <Link href="/" key="1">
                    <a className="mr-4 p-6">Home</a>
                </Link>
                <Link href="/commit" key="4">
                    <a className="mr-4 p-6">Commit</a>
                </Link>
                <Link href="/set-up" key="2">
                    <a className="mr-4 p-6">Set Up</a>
                </Link>
                <Link href="/testcase" key="3">
                    <a target="_blank" className="mr-4 p-6">
                        TestCase
                    </a>
                </Link>
                <ConnectButton moralisAuth={false} />
            </div>
        </div>
    )
}
