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
import Image from "next/image"
import clsx from "clsx"
const imageLoader = ({ src, width, quality }: any) => {
    return `../../background.jpg`
}
//import backgroundImage from "../../public/background.jpg"

export function BackgroundImage({
    className,
    position = "left",
}: {
    className?: string
    position?: "left" | "right"
}) {
    return (
        <div className={clsx("absolute inset-0 overflow-hidden bg-indigo-50", className)}>
            <Image
                className="opacity-20"
                src="../../background.jpg"
                loader={imageLoader}
                alt=""
                width={918}
                height={1495}
                priority
                unoptimized
            />
            <div className="absolute inset-x-0 top-0 h-40 bg-gradient-to-b from-white" />
            <div className="absolute inset-x-0 bottom-0 h-40 bg-gradient-to-t from-white" />
        </div>
    )
}
