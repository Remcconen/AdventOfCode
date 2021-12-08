from os import sep
import numpy as np

def read_input(file):
    f = open(file, "r")
    crabs = np.fromstring(f.readline(), dtype=int, sep=',')
    return crabs


def solve_1(crabs):
    return min([sum(map(lambda crab: abs(crab-i), crabs)) for i in range(max(crabs))])

def solve_2(crabs):
    return min([sum(map(lambda crab: (abs(crab-i)*(abs(crab-i)+1)/2), crabs)) for i in range(max(crabs))])
        


crabs = read_input("2021/7/input.txt")
print("Solution 1:", solve_1(crabs))
print("Solution 2:", solve_2(crabs))