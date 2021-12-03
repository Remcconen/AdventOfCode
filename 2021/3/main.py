from bitstring import BitArray

def getBaseBit(length):
    f = "#0"+str(length)+"b"
    return BitArray(bin=format(1, f))

def read_input(file):
    f = open(file, "r")
    lines = f.readlines()
    result = []
    for line in lines:
        result.append(BitArray(bin=line.rstrip()))
    return result


def count_bits(input):
    length = len(input[0])

    result = []
    for i in range(0, length):
        result.append(count_bit(input, i))
    
    return result

def count_bit(input, index):
    length = len(input[0])
    baseBit = getBaseBit(length+2)
    result = 0
    for number in input:
        if (number & (baseBit << index)):
            result += 1

    return result

def find_common(input, mostCommon):
    length = len(input[0])
    baseBit = getBaseBit(length+2)
    result = input.copy()

    # Handle each bit
    for index in reversed(range(0, length)):

        internalResult = result.copy()
        result = []

        inputLength = len(internalResult)
        if len(internalResult) == 1:
            return internalResult

        # Count bit and determine if bit == 1 should be kept
        bitCount = count_bit(internalResult, index)
        bitKeep = False
        if bitCount > (inputLength / 2):
            bitKeep = True
        elif bitCount == (inputLength / 2):
            bitKeep = True

        if not mostCommon:
            bitKeep = not bitKeep

        # Handle remaining result
        for i in range(0, len(internalResult)):
            hasBit = internalResult[i] & (baseBit << index)
            if (bitKeep and hasBit):
                result.append(internalResult[i])
            elif (not bitKeep) & (not hasBit):
                result.append(internalResult[i])
                
    return result


def solve_1(input):
    inputLength = len(input)
    bitCounts = count_bits(input)

    result = ""
    for count in bitCounts:
        if (count > (inputLength/2)):
            result = "1"+result
        else:
            result = "0"+result

    return int(result, 2) * (~BitArray(bin=result)).uint


def solve_2(input):
    oxygen = find_common(input, True)
    co2 = find_common(input, False)

    return oxygen[0].uint * co2[0].uint

input = read_input("2021/3/input.txt")
print("Solution 1:", solve_1(input))
print("Solution 2:", solve_2(input))