import numpy as np

def read_input(input):
    f = open(input, "r")
    timers = np.fromstring(f.readline().rstrip(), dtype=int, sep=',')
    
    return timers


def solve(timers, max_days):
    result = np.zeros(7)
    for timer in timers:
        result[timer] += 1

    fish7 = 0
    fish8 = 0
    for i in range (0, max_days):
        newFish = result[0]
        result = np.roll(result, -1)
        result[6] += fish7
        fish7 = fish8
        fish8 = newFish

    return np.sum(result)+fish7+fish8


input = read_input("2021/6/input.txt")
print("Solution 1:",solve(input, 80))
print("Solution 2:",solve(input, 256))