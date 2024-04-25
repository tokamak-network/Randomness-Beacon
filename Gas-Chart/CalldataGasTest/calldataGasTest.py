# Copyright 2024 justin
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import math

# first word is fixed to 00000000000000000000000000000000000000000000000000000000000000e0
parameterCount = 7
offSetOfFirstParam = parameterCount * 32

# 여기는 무조건 0x00..e0 값으로 고정이다 왜냐하면, 7개의 파라미터값이 고정이기 때문. 7 * 0x20 을 하면 0xe0이 된다. 그래서 32byte중에서 1바이트만 Non-zero, 나머지는 zero이기 때문에 상수다
offSetOfFirstParamGasUsed = 31 * 4 + 1 * 16


# eg. (256bits + 7) // 8 => 32bytes, (257bits + 7) // 8 => 33bytes
def getBytesLengthfromBitLength(bitLength):
  return (bitLength + 7) // 8


# eg. (32bytes + 31) // 32 => 1 word, (33bytes + 31) // 32 => 2 words
def getByteWordsfromBytesLength(bytesLength):
  return (bytesLength + 31) // 32


def getByteWordOfBigNumberValData(l):  #l은 Lambda, Eg. 2048의 byteWord는 8.
  return getByteWordsfromBytesLength(getBytesLengthfromBitLength(l))


#word는 EVM 메모리 단위, 1word=32bytes, 2word = 64bytes...
def getByteWordOfWholeBigNumber(l):
  offSetAndBitlenAndLength = 3  # offset, bitlen, length는 무조건 3 bytesword로 고정이다.
  return 3 + getByteWordOfBigNumberValData(
      l)  # lambda bit에 따라서 해당 data의 bytesword를 구한다.


def getOffsetValueOfithParam(t, d, l, i):
  # 32를 곱하는 것은 32bytes 라는 뜻. 즉 Offset은 bytes 단위다.
  # 32*8 에서 8은, 앞에 8개 word가 fixed, spreadsheet의 index 0~7, 즉 8개가 고정이다.
  # 32*8(t - d)은 offset to start of data part of the element of array 부분, spreadsheet index 8~20에 해당한다. t-d는 Proof의 길이다.
  # 32 * (getByteWordOfWholeBigNumber(l) * (t - d + i - 1)), getByteWordOfWholeBigNumber는 1개의 BigNumber struct의 총 byte개수, (t - d + i - 1)에서 t-d는 proof의 길이, i - 1은 몇번째의 offset을 구하는 건지
  return (32 * 8) + 32 * (t - d) + 32 * (getByteWordOfWholeBigNumber(l) *
                                         (t - d + i - 1))


#offset 자체의 값을 구하는 함수
def getOffsetValueOfithElementOfArray(t, d, l, i):
  # 32 * (t-d)는 proof의 길이
  # i는 몇번째의 offset을 구하는 건지
  # l은 Lambda, eg. 2048bit.
  return 32 * (t - d) + 32 * getByteWordOfWholeBigNumber(l) * i


def getHex(t):
  return hex(t)


def getBigLength(value):
  return math.log2(value) + 1


def getGasUsedOfXBytes(x):
  bytesLengthOfValue = x
  chanceOfBeingZeroByte = (1 / 256)  # 1byte가 zero-byte일 확률
  chanceOfBeingNonZeroByte = (255 / 256)  # 1byte가 non-zero-byte일 확률
  a = 0
  b = 0

  # 해당 값의 bytes 길이를 구하고, 최상위 한 바이트는 무조건 non-zero다. 그래서 1*16을 한다.
  # 그리고 해당 값의 Bytes 길이 - 1은 확률적으로 zero-byte와 non-zerobyte가 존재한다.
  a = 1 * 16 + (bytesLengthOfValue - 1) * chanceOfBeingNonZeroByte * 16 + (
      bytesLengthOfValue - 1) * chanceOfBeingZeroByte * 4
  # 32bytes중에서 해당 값의 bytes 길이 값을 뺀 byte들은 무조건 zero byte다.
  b = (32 - bytesLengthOfValue) * 4
  return a + b


def getGasUsedOf32BytesValue(value):
  bytesLengthOfValue = getBytesLengthfromBitLength(
      getBigLength(value))  #해당 값의 bytes 길이를 구한다.
  return getGasUsedOfXBytes(bytesLengthOfValue)


def getGasUsedOfOffset(t, d, l, i):
  value = getOffsetValueOfithParam(
      t, d, l, i
  )  # t,d,l,i를 통해서 진짜 offset to the start of each parameter data area 값을 구할 수 있다.
  return getGasUsedOf32BytesValue(value)  # 해당 값의 gasUsed를 확률적으로 계산한다.


def getPaddedBytesLength(bytesLength):
  return (bytesLength + 31) // 32 * 32


# BigNumber struct의 gasUsed를 구한다.
def getGasUsedOfBigNumber(lambd):
  gasUsedOfOffsetToStartOfValOfBigNumber = 31 * 4 + 1 * 16  #무조건 0x40으로 고정 이므로 1byte만 non-zero
  gasUsedOfBitlenOfBigNumber = getGasUsedOf32BytesValue(
      lambd)  # 계산의 편의를 위해, bitlen을 2048로 고정한다. 대부분 2bytes가 non-zero다.
  gasUsedOfLengthOfBigNumber = getGasUsedOf32BytesValue(
      getPaddedBytesLength(getBytesLengthfromBitLength(lambd))
  )  # 이것은 Length of the data in bytes 인데, 오프체인에서 left-padding을 넣어줬으므로 여기서도 padding 값을 고려해서 gasUsed를 구한다.

  leftBytes = 0  # 2048, 3072처럼 딱 32bytes단위로 떨어지지 않을때, 나머지 bytes 다. (2048, 3072는 딱 떨어진다.), 나머지 bytes는 따로 가스비를 측정한다.
  if (lambd % 32 == 0):
    leftBytes = 32
  else:
    leftBytes = lambd % 32

  numOfZeroBytesOf32BytesProbabilistically = (32 / 256
                                              )  # 32bytes중에 zero-bytes 확률적 갯수
  numOfNonZeroBytesOf32BytesProbabilistically = 32 * (
      255 / 256)  # 32bytes중에 non-zero bytes 확률적 갯수
  gasUsedOf32Bytesdata = (4 * numOfZeroBytesOf32BytesProbabilistically +
                          16 * numOfNonZeroBytesOf32BytesProbabilistically)

  gasUsedOfValOfBigNumber = gasUsedOf32Bytesdata * (
      getByteWordOfBigNumberValData(lambd) - 1)

  gasUsedOfLeftBytes = getGasUsedOfXBytes(leftBytes)

  #모두 더한다.
  gasUsedOfBigNumber = gasUsedOfOffsetToStartOfValOfBigNumber
  gasUsedOfBigNumber += gasUsedOfBitlenOfBigNumber
  gasUsedOfBigNumber += gasUsedOfLengthOfBigNumber
  gasUsedOfBigNumber += gasUsedOfValOfBigNumber
  gasUsedOfBigNumber += gasUsedOfLeftBytes
  return gasUsedOfBigNumber


def totalGasUsed(delta):
  ###
  t = 22
  lambd = 2048

  if (delta == 0):
    t += 1

  gasUsed = offSetOfFirstParamGasUsed
  for i in range(1, 5):  # i는 1~4, spreadsheet의 index 1~4에 해당한다.
    gasUsed += getGasUsedOfOffset(t, delta, lambd, i)

  gasUsedOftowPowerOfDelta = 31 * 4 + 1 * 16  #2의 거듭제곱 형태이기 때문에 1byte만 non-zero
  gasUsedOfT = 31 * 4 + 1 * 16  #2의 거듭제곱 형태이기 때문에 1byte만 non-zero
  gasUsed += gasUsedOftowPowerOfDelta
  gasUsed += gasUsedOfT

  gasUsed += getGasUsedOf32BytesValue(t - delta)
  for i in range(t - delta):  # i는 0~proof의 길이, spreadsheet의 index 8~20에 해당한다.
    gasUsed += getGasUsedOf32BytesValue(
        getOffsetValueOfithElementOfArray(t, delta, lambd, i))
  # t - delta (=proof의 길이) + 3(3은 x,y,n를 뜻함), spreadsheet에서 index 21~199에 해당한다.
  gasUsed += (getGasUsedOfBigNumber(lambd) * (t - delta + 3))

  gasUsedOfLengthOfTwoPowerOfDeltaBytes = 31 * 4 + 1 * 16  # 이 값은 twoPowerOfDeltaBytes의 bytes길이를 나타내는 값으로 무조건 0x20으로 고정이다. 그러므로 1byte만 non-zero, spreadsheet index의 197
  gasUsedOfDataOfTwoPowerOfDeltaBytes = 31 * 4 + 1 * 16  # 이 값은 twoPowerOfDeltaBytes의 값으로 2의 거듭제곱 형태이므로 무조건 1byte만 Non-zero다.

  gasUsed += gasUsedOfLengthOfTwoPowerOfDeltaBytes
  gasUsed += gasUsedOfDataOfTwoPowerOfDeltaBytes
  return gasUsed


for delta in range(21, -1, -1):  #delta를 21부터 0까지 테스트
  Gtransaction = 21000  # 고정 가스비
  functionSelectorGasUsed = 16 * 4  #함수 셀렉터 고정 가스비, zero-byte가 포함될 수도 있지만 저희 테스트케이스에서는 모두 non-zero
  print("intrinsic gas when delta:", delta, "= ",
        totalGasUsed(delta) + Gtransaction + functionSelectorGasUsed)
