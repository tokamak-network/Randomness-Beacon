import math

# first word is fixed to 00000000000000000000000000000000000000000000000000000000000000c0
# This is always fixed to 0x00..c0 because the number 6 parameter values are fixed. 6 * 0x20 will be 0xc0. So out of 32 bytes, only 1 byte is non-zero and the rest are zero, so it is constant.
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
  # 32*7 에서 7은, 앞에 7개 word가 fixed, spreadsheet의 index 0~6, 즉 7개가 고정이다.
  # 32*(t - d)은 offset to start of data part of the element of array 부분, spreadsheet index 7~19에 해당한다. t-d는 Proof의 길이다.
  # 32 * (getByteWordOfWholeBigNumber(l) * (t - d + i - 1)), getByteWordOfWholeBigNumber는 1개의 BigNumber struct의 총 byte개수, (t - d + i - 1)에서 t-d는 proof의 길이, i - 1은 몇번째의 offset을 구하는 건지
  return (32 * 7) + 32 * (t - d) + 32 * (getByteWordOfWholeBigNumber(l) *
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
  # print("dd", math.log2(value) + 1)
  if value == 0:
    return 0
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
  t = 25
  lambd = 3072

  #print(t - delta)

  gasUsed = offSetOfFirstParamGasUsed

  for i in range(1, 4):  # i는 1~3, spreadsheet의 index 1~3에 해당한다.
    gasUsed += getGasUsedOfOffset(t, delta, lambd, i)

  gasUsedOfDelta = 31 * 4 + 1 * 16  #delta값은 decimal로 0~25사이의 값, 1byte로 충분하다.
  gasUsedOfT = 31 * 4 + 1 * 16  #2의 거듭제곱 형태이기 때문에 1byte만 non-zero
  gasUsed += gasUsedOfDelta
  gasUsed += gasUsedOfT

  gasUsed += getGasUsedOf32BytesValue(t - delta)  # length of v array

  for i in range(t - delta):  # i는 0~proof의 길이, spreadsheet의 index 7~19에 해당한다.
    gasUsed += getGasUsedOf32BytesValue(
        getOffsetValueOfithElementOfArray(t, delta, lambd, i))
  # t - delta (=proof의 길이) + 3(3은 x,y,n를 뜻함), spreadsheet에서 index 20~195에 해당한다.
  gasUsed += (getGasUsedOfBigNumber(lambd) * (t - delta + 3))
  return gasUsed


for delta in range(0, 26):  #delta를 21부터 0까지 테스트
  Gtransaction = 21000  # 고정 가스비
  functionSelectorGasUsed = 16 * 4  #함수 셀렉터 고정 가스비, zero-byte가 포함될 수도 있지만 저희 테스트케이스에서는 모두 non-zero
  # print("intrinsic gas when delta:", delta, "= ",
  #       totalGasUsed(delta) + Gtransaction + functionSelectorGasUsed)
  print(totalGasUsed(delta) + Gtransaction + functionSelectorGasUsed)
