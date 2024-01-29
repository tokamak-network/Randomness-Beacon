import { ethers, BigNumberish } from "ethers"

import { VDFClaim, TestCase, BigNumber } from "./interfaces"
import testData from "./data_20231212_150019.json"

export const createTestCases2 = () => {
    const result: TestCase[] = []
    let ts: TestCase
    let setUpProofs: VDFClaim[] = []
    let recoveryProofs: VDFClaim[] = []
    let randomList: BigNumber[] = []
    let commitList: BigNumber[] = []
    for (let i = 0; i < (testData.setupProofs as []).length; i++) {
        setUpProofs.push({
            x: {
                //val: toBeHex(testcase[4][i][1]),
                // val: toBeHex(
                //     testData.setupProofs[i].x,
                //     getLength(dataLength(toBeHex(testData.setupProofs[i].x)))
                // ),
                val: ethers.utils.hexZeroPad(
                    ethers.utils.hexlify(testData.setupProofs[i].x),
                    getLength(
                        ethers.utils.hexDataLength(ethers.utils.hexlify(testData.setupProofs[i].x))
                    )
                ),
                bitlen: getBitLenth2(testData.setupProofs[i].x),
            },
            y: {
                val: ethers.utils.hexZeroPad(
                    ethers.utils.hexlify(testData.setupProofs[i].y),
                    getLength(
                        ethers.utils.hexDataLength(ethers.utils.hexlify(testData.setupProofs[i].y))
                    )
                ),
                bitlen: getBitLenth2(testData.setupProofs[i].y),
            },
            T: testData.setupProofs[i].T,
            v: {
                val: ethers.utils.hexZeroPad(
                    ethers.utils.hexlify(testData.setupProofs[i].v),
                    getLength(
                        ethers.utils.hexDataLength(ethers.utils.hexlify(testData.setupProofs[i].v))
                    )
                ),
                bitlen: getBitLenth2(testData.setupProofs[i].v),
            },
        })
    }
    for (let i = 0; i < (testData.recoveryProofs as []).length; i++) {
        recoveryProofs.push({
            x: {
                val: ethers.utils.hexZeroPad(
                    ethers.utils.hexlify(testData.recoveryProofs[i].x),
                    getLength(
                        ethers.utils.hexDataLength(
                            ethers.utils.hexlify(testData.recoveryProofs[i].x)
                        )
                    )
                ),
                bitlen: getBitLenth2(testData.recoveryProofs[i].x),
            },
            y: {
                val: ethers.utils.hexZeroPad(
                    ethers.utils.hexlify(testData.recoveryProofs[i].y),
                    getLength(
                        ethers.utils.hexDataLength(
                            ethers.utils.hexlify(testData.recoveryProofs[i].y)
                        )
                    )
                ),
                bitlen: getBitLenth2(testData.recoveryProofs[i].y),
            },
            T: testData.recoveryProofs[i].T,
            v: {
                val: ethers.utils.hexZeroPad(
                    ethers.utils.hexlify(testData.recoveryProofs[i].v),
                    getLength(
                        ethers.utils.hexDataLength(
                            ethers.utils.hexlify(testData.recoveryProofs[i].v)
                        )
                    )
                ),
                bitlen: getBitLenth2(testData.recoveryProofs[i].v),
            },
        })
    }
    for (let i = 0; i < (testData.randomList as []).length; i++) {
        randomList.push({
            val: ethers.utils.hexZeroPad(
                ethers.utils.hexlify(testData.randomList[i]),
                getLength(ethers.utils.hexDataLength(ethers.utils.hexlify(testData.randomList[i])))
            ),
            bitlen: getBitLenth2(testData.randomList[i]),
        })
    }
    for (let i = 0; i < (testData.commitList as []).length; i++) {
        commitList.push({
            val: ethers.utils.hexZeroPad(
                ethers.utils.hexlify(testData.commitList[i]),
                getLength(ethers.utils.hexDataLength(ethers.utils.hexlify(testData.commitList[i])))
            ),
            bitlen: getBitLenth2(testData.commitList[i]),
        })
    }
    result.push({
        n: {
            val: ethers.utils.hexZeroPad(
                ethers.utils.hexlify(testData.n),
                getLength(ethers.utils.hexDataLength(ethers.utils.hexlify(testData.n)))
            ),
            bitlen: getBitLenth2(testData.n),
        },
        g: {
            val: ethers.utils.hexZeroPad(
                ethers.utils.hexlify(testData.g),
                getLength(ethers.utils.hexDataLength(ethers.utils.hexlify(testData.g)))
            ),
            bitlen: getBitLenth2(testData.g),
        },
        h: {
            val: ethers.utils.hexZeroPad(
                ethers.utils.hexlify(testData.h),
                getLength(ethers.utils.hexDataLength(ethers.utils.hexlify(testData.h)))
            ),
            bitlen: getBitLenth2(testData.h),
        },
        T: testData.T,
        setupProofs: setUpProofs,
        randomList: randomList,
        commitList: commitList,
        omega: {
            val: ethers.utils.hexZeroPad(
                ethers.utils.hexlify(testData.omega),
                getLength(ethers.utils.hexDataLength(ethers.utils.hexlify(testData.omega)))
            ),
            bitlen: getBitLenth2(testData.omega),
        },
        recoveredOmega: {
            val: ethers.utils.hexZeroPad(
                ethers.utils.hexlify(testData.recoveredOmega),
                getLength(
                    ethers.utils.hexDataLength(ethers.utils.hexlify(testData.recoveredOmega))
                )
            ),
            bitlen: getBitLenth2(testData.recoveredOmega),
        },
        recoveryProofs: recoveryProofs,
    })

    return result
}

export const getBitLenth2 = (num: string): BigNumberish => {
    return BigInt(num).toString(2).length
}

const getBitLenth = (num: bigint): BigNumberish => {
    return num.toString(2).length
}

export const getLength = (value: number): number => {
    let length: number = 32
    while (length < value) length += 32
    return length
}
