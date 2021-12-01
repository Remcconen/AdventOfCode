def solve_1(input):
    result = 0
    for i in range(1, len(input)):
        if input[i] > input[i-1]:
            result += 1
    return result

def solve_2(input):
    result = 0
    for i in range(3, len(input)):
        if (input[i] + input[i-1] + input[i-2]) > (input[i-1] + input[i-2] + input[i-3]):
            result += 1
    return result

def read_input():
    f = open("input.txt", "r")
    lines = f.readlines()
    result = []
    for line in lines:
        result.append(int(line))
    return result

test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
input = read_input()

print("Solution 1:", solve_1(input))
print("Solution 2:", solve_2(input))