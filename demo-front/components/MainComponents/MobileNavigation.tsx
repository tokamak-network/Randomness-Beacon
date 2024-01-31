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
import { Popover, Transition } from "@headlessui/react"
import dynamic from "next/dynamic"
import Link from "next/link"
import clsx from "clsx"
import { Fragment } from "react"
function MobileNavLink({
    href,
    children,
    target,
}: {
    href: string
    children: string
    target?: string
}) {
    return (
        <Link href={href}>
            <Popover.Button>
                <a className="block w-full p-2 text-left" target={target}>
                    {children}
                </a>
            </Popover.Button>
        </Link>
    )
}

function MobileNavIcon({ open }: { open: boolean }) {
    return (
        <svg
            aria-hidden="true"
            className="h-3.5 w-3.5 overflow-visible stroke-slate-700"
            fill="none"
            strokeWidth={2}
            strokeLinecap="round"
        >
            <path
                d="M0 1H14M0 7H14M0 13H14"
                className={clsx("origin-center transition", open && "scale-90 opacity-0")}
            />
            <path
                d="M2 2L12 12M12 2L2 12"
                className={clsx("origin-center transition", !open && "scale-90 opacity-0")}
            />
        </svg>
    )
}
export default function MobileNavigation() {
    return (
        <Popover>
            <Popover.Button
                className="relative z-10 flex h-8 w-8 items-center justify-center ui-not-focus-visible:outline-none"
                aria-label="Toggle Navigation"
            >
                {({ open }) => <MobileNavIcon open={open} />}
            </Popover.Button>
            <Transition.Root>
                <Transition.Child
                    as={Fragment}
                    enter="duration-150 ease-out"
                    enterFrom="opacity-0"
                    enterTo="opacity-100"
                    leave="duration-150 ease-in"
                    leaveFrom="opacity-100"
                    leaveTo="opacity-0"
                >
                    <Popover.Overlay className="fixed inset-0 bg-slate-300/50" />
                </Transition.Child>
                <Transition.Child
                    as={Fragment}
                    enter="duration-150 ease-out"
                    enterFrom="opacity-0 scale-95"
                    enterTo="opacity-100 scale-100"
                    leave="duration-100 ease-in"
                    leaveFrom="opacity-100 scale-100"
                    leaveTo="opacity-0 scale-95"
                >
                    <Popover.Panel
                        as="div"
                        className="absolute inset-x-0 top-full mt-4 flex origin-top flex-col rounded-2xl bg-white p-4 text-lg tracking-tight text-slate-900 shadow-xl ring-1 ring-slate-900/5"
                    >
                        <MobileNavLink href="/">Home</MobileNavLink>
                        <MobileNavLink href="/commit">Commit</MobileNavLink>
                        <MobileNavLink href="/set-up">SetUp</MobileNavLink>
                        <hr className="m-2 border-slate-300/40" />
                        <MobileNavLink href="/testcase" target="_blank">
                            TestCase
                        </MobileNavLink>
                    </Popover.Panel>
                </Transition.Child>
            </Transition.Root>
        </Popover>
    )
}
