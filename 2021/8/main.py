def read_input(file):
    f = open(file, "r")
    digits = []
    signals = []
    for line in f.readlines():
        digits.append(list(map(lambda x: set(sorted(x)), line.split('|')[0].rstrip().split(" "))))
        signals.append(list(map(lambda x: set(sorted(x)), line.split('|')[1].strip().split(" "))))
    
    return digits, signals


# 0:    len 6
# 1: len 2
# 2:        len 5
# 3:        len 5
# 4: len 4
# 5:        len 5
# 6:    len 6
# 7: len 3
# 8: len 7
# 9:    len 6
def get_numbers(digits):
    numbers = [None] * 10

    numbers[1] = next(digit for digit in digits if len(digit) == 2)
    numbers[4] = next(digit for digit in digits if len(digit) == 4)
    numbers[7] = next(digit for digit in digits if len(digit) == 3)
    numbers[8] = next(digit for digit in digits if len(digit) == 7)

    numbers[9] = next(digit for digit in digits if len(digit) == 6 and (numbers[4] | numbers[7]).issubset(digit))
    numbers[5] = next(digit for digit in digits if len(digit) == 5 and digit.issubset(numbers[9]) and not numbers[1].issubset(digit))

    numbers[6] = next(digit for digit in digits if len(digit) == 6 and len(digit - numbers[5]) == 1 and digit != numbers[9])
    numbers[0] = next(digit for digit in digits if len(digit) == 6 and digit != numbers[9] and digit != numbers[6])

    numbers[3] = next(digit for digit in digits if len(digit) == 5 and len(numbers[9] - digit) == 1 and digit != numbers[5])
    numbers[2] = next(digit for digit in digits if len(digit) == 5 and digit != numbers[3] and digit != numbers[5])                                                  

    return numbers

def calculate_signal(digits, signal):
    numbers = get_numbers(digits)
    result = ""

    for s in signal:
        result += str(numbers.index(s))

    return result


def solve_1(signals):
    return len(list(filter(lambda signal: len(signal) in [2, 4, 3, 7], [x for y in signals for x in y] )))

def solve_2(digits, signals):
    sum = 0
    for i in range(0, len(digits)):
        sum += int(calculate_signal(digits[i], signals[i]))

    return sum


digits, signals = read_input("2021/8/input.txt")
print("Solution 1:",solve_1(signals))
print("Solution 2:",solve_2(digits, signals))
