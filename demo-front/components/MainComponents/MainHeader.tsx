// Copyright 2024 justin
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
"use client"
import dynamic from "next/dynamic"
import React, { useEffect, useState } from "react"
import Link from "next/link"
import MobileNavigation from "./MobileNavigation"
import { ConnectButton } from "web3uikit"
import { Container } from "./Container"
import Image from "next/image"
import { NavLink } from "./NavLink"
const imageLoader = ({ src, width, quality }: any) => {
    return `../tokamaklogo.png`
}

export function MainHeader() {
    const [rerender, setRerender] = useState(false)
    useEffect(() => {
        setRerender(true)
    }, [])
    return (
        <header className="py-10">
            <Container>
                <nav className="relative z-50 flex justify-between">
                    <div className="flex items-center md:gap-x-12">
                        <div className="h-10 w-auto">
                            <Link href="/" key="5">
                                <a className="flex flex-row items-center">
                                    <div className="min-w-fit">
                                        <Image
                                            src="../tokamaklogo.png"
                                            loader={imageLoader}
                                            width={45}
                                            height={35}
                                            alt="Picture of the author"
                                        />
                                    </div>
                                    <div className="pl-2 font-bold text-xl mb-2 mr-5">
                                        <span className="hidden lg:inline whitespace-nowrap">
                                            TON Random Airdrop
                                        </span>
                                    </div>
                                </a>
                            </Link>
                        </div>
                        <div className="hidden md:flex md:gap-x-6">
                            <NavLink href="/">
                                <span>Home</span>
                            </NavLink>
                            <NavLink href="/commit">
                                <span>Commit</span>
                            </NavLink>
                            <NavLink href="/set-up">
                                <span>SetUp</span>
                            </NavLink>
                            <NavLink href="/testcase" target="_blank">
                                <span>TestCase</span>
                            </NavLink>
                        </div>
                    </div>
                    <div className="flex items-center gap-x-3 md:gap-x-8">
                        <div className="md:block">
                            <ConnectButton moralisAuth={false} />
                        </div>
                        <div className="-mr-1 md:hidden">
                            {/* {rerender ? <MobileNavigation /> : <></>} */}
                        </div>
                    </div>
                </nav>
            </Container>
        </header>
    )
}
