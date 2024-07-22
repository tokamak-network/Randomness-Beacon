// Copyright 2024 justin
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
import { BigNumberish } from "ethers"
import { Table, Tag } from "web3uikit"
import { Container } from "./Container"
export function RequestTables({
    requestIds,
    randomNums,
    threeClosestToSevenHundred,
}: {
    requestIds: BigNumberish[]
    randomNums: BigNumberish[]
    threeClosestToSevenHundred: any
}) {
    const getSecondTableContens: any = []
    function getPrizeAmount(threeClosestToSevenHundred: any) {
        if (threeClosestToSevenHundred == undefined) return
        const rticks = []
        const gaps = [1000, 1000, 1000, 1000]
        for (let i = 0; i < threeClosestToSevenHundred[0]?.length; i++) {
            if (threeClosestToSevenHundred[0][i].toString() != "1001") {
                getSecondTableContens.push([
                    threeClosestToSevenHundred[0][i].toString(),
                    threeClosestToSevenHundred[1][i].toString(),
                ])
                rticks.push(threeClosestToSevenHundred[0][i])
                gaps[i] = Math.abs(Number(threeClosestToSevenHundred[0][i]) - 700)
            }
        }
        const counts: any = threeClosestToSevenHundred[1] as any
        const TOTALPRIZE = 1000
        const FIRSTPRIZE = 550
        const SECONDPRIZE = 300
        const THIRDPRIZE = 150
        if (counts == undefined) return
        if (getSecondTableContens.length < 1) return
        if (gaps[0] == gaps[1]) {
            const firstCount = Number(counts[0].toString()) + Number(counts[1].toString())
            if (firstCount > 2) {
                const eachPrize = Math.floor(TOTALPRIZE / firstCount)
                if (getSecondTableContens.length < 2) return
                for (let i = 0; i < 2; i++) {
                    getSecondTableContens[i].push(eachPrize.toString() + " TON")
                }
                return
            } else if (firstCount == 2) {
                if (getSecondTableContens.length < 2) return
                const eachPrize = Math.floor((FIRSTPRIZE + SECONDPRIZE) / 2)
                getSecondTableContens[0].push(eachPrize.toString() + " TON")
                getSecondTableContens[1].push(eachPrize.toString() + " TON")
                if (getSecondTableContens.length < 3) return
                if (gaps[2] == gaps[3]) {
                    const thirdCount = Number(counts[2].toString()) + Number(counts[3].toString())
                    const eachPrize = Math.floor(THIRDPRIZE / thirdCount)
                    if (getSecondTableContens.length < 4) return
                    for (let i = 2; i < 4; i++) {
                        getSecondTableContens[i].push(eachPrize.toString() + " TON")
                    }
                    return
                } else {
                    if (getSecondTableContens.length < 3) return
                    const thirdCount = Number(counts[2].toString())
                    const eachPrize = Math.floor(THIRDPRIZE / thirdCount)
                    if (getSecondTableContens.length < 3) return
                    getSecondTableContens[2].push(eachPrize.toString() + " TON")
                    return
                }
            }
        } else {
            const firstCount = Number(counts[0].toString())
            if (getSecondTableContens.length < 1) return
            if (firstCount > 2) {
                const eachPrize = Math.floor(TOTALPRIZE / firstCount)
                if (getSecondTableContens.length < 1) return
                getSecondTableContens[0].push(eachPrize.toString() + " TON")
                return
            } else if (firstCount == 2) {
                const eachPrize = Math.floor((FIRSTPRIZE + SECONDPRIZE) / 2)
                if (getSecondTableContens.length < 2) return
                getSecondTableContens[0].push(eachPrize.toString() + " TON")
                if (gaps[1] == gaps[2]) {
                    if (getSecondTableContens.length < 3) return
                    const secondCount = Number(counts[1].toString()) + Number(counts[2].toString())
                    const eachPrize = Math.floor(THIRDPRIZE / secondCount)
                    if (getSecondTableContens.length < 3) return
                    for (let i = 1; i < 3; i++) {
                        getSecondTableContens[i].push(eachPrize.toString() + " TON")
                    }
                    return
                } else {
                    const secondCount = Number(counts[1].toString())
                    if (getSecondTableContens.length < 2) return
                    if (secondCount > 1) {
                        const eachPrize = Math.floor(THIRDPRIZE / secondCount)
                        getSecondTableContens[1].push(eachPrize.toString() + " TON")
                        return
                    } else if (secondCount == 1) {
                        getSecondTableContens[1].push(THIRDPRIZE.toString() + " TON")
                    }
                }
            } else {
                if (getSecondTableContens.length < 1) return
                getSecondTableContens[0].push(FIRSTPRIZE.toString() + " TON")
                if (gaps[1] == gaps[2]) {
                    const secondCount = Number(counts[1].toString()) + Number(counts[2].toString())
                    const eachPrize = Math.floor((SECONDPRIZE + THIRDPRIZE) / secondCount)
                    if (getSecondTableContens.length < 3) return
                    for (let i = 1; i < 3; i++) {
                        getSecondTableContens[i].push(eachPrize.toString() + " TON")
                    }
                    return
                } else {
                    const secondCount = Number(counts[1].toString())
                    if (secondCount > 1) {
                        const eachPrize = Math.floor((SECONDPRIZE + THIRDPRIZE) / secondCount)
                        if (getSecondTableContens.length < 2) return
                        getSecondTableContens[1].push(eachPrize.toString() + " TON")
                        return
                    } else if (secondCount == 1) {
                        if (getSecondTableContens.length < 2) return
                        getSecondTableContens[1].push(SECONDPRIZE.toString() + " TON")
                        if (gaps[2] == gaps[3]) {
                            const thirdCount =
                                Number(counts[2].toString()) + Number(counts[3].toString())
                            const eachPrize = Math.floor(THIRDPRIZE / thirdCount)
                            if (getSecondTableContens.length < 4) return
                            for (let i = 2; i < 4; i++) {
                                getSecondTableContens[i].push(eachPrize.toString() + " TON")
                            }
                            return
                        } else {
                            const thirdCount = Number(counts[2].toString())
                            if (thirdCount > 1) {
                                const eachPrize = Math.floor(THIRDPRIZE / thirdCount)
                                if (getSecondTableContens.length < 3) return
                                getSecondTableContens[2].push(eachPrize.toString() + " TON")
                                return
                            } else if (thirdCount == 1) {
                                if (getSecondTableContens.length < 3) return
                                getSecondTableContens[2].push(THIRDPRIZE.toString() + " TON")
                            }
                        }
                    }
                }
            }
        }
    }

    const getTableContents: any = []
    for (let i = 0; i < requestIds?.length; i++) {
        getTableContents.push([requestIds[i].toString()])
    }
    for (let i = 0; i < randomNums?.length; i++) {
        getTableContents[i].push(<Tag color="blue" text="fulfilled" />, randomNums[i].toString())
    }
    for (let i = randomNums.length; i < requestIds?.length; i++) {
        getTableContents[i].push(<Tag color="red" text="pending" />, "")
    }
    getPrizeAmount(threeClosestToSevenHundred)
    return (
        <div>
            <Container className="relative pb-3.5">
                {requestIds.length > 0 ? (
                    <>
                        {" "}
                        <div className="mb-6 space-y-6 font-display text-2xl tracking-tight text-blue-900">
                            <div>My Request Info</div>
                        </div>
                        <Table
                            columnsConfig="1fr 1fr 1fr"
                            data={getTableContents}
                            header={[
                                <span>RequestId</span>,
                                <span>Status</span>,
                                <span>RandomNumber</span>,
                            ]}
                            isColumnSortable={[true, false, false]}
                            maxPages={Math.ceil(requestIds.length / 5)}
                            onPageNumberChanged={function noRefCheck() {}}
                            onRowClick={function noRefCheck() {}}
                            pageSize={5}
                        />
                    </>
                ) : (
                    <> </>
                )}

                {getSecondTableContens.length > 0 ? (
                    <>
                        <div className="mt-6 mb-6 space-y-6 font-display text-2xl tracking-tight text-blue-900">
                            <div>Currently eligible for prizes</div>
                        </div>
                        <Table
                            columnsConfig="1fr 1fr 1fr"
                            data={getSecondTableContens}
                            header={[
                                <span>Random Number</span>,
                                <span>Number of people with this random number</span>,
                                <span>Prize Amount</span>,
                            ]}
                            isColumnSortable={[false, false, false]}
                            maxPages={Math.ceil(requestIds.length / 5)}
                            onPageNumberChanged={function noRefCheck() {}}
                            onRowClick={function noRefCheck() {}}
                            pageSize={5}
                        />
                    </>
                ) : (
                    <></>
                )}
            </Container>
        </div>
    )
}
