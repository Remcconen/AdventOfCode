import re
import numpy as np

def read_input(input):
    regex = "(\d+),(\d+) -> (\d+),(\d+)"
    max_x = 0
    max_y = 0
    coords = []

    f = open(input, "r")
    for line in f.readlines():
        match = re.search(regex, line)
        x1 = int(match.group(1))
        y1 = int(match.group(2))
        x2 = int(match.group(3))
        y2 = int(match.group(4))
        max_x = max(x1, x2, max_x)
        max_y = max(y1, y2, max_y)

        coords.append([[x1, y1], [x2, y2]])

    return max_x, max_y, coords

def solve_1(coords, max_x, max_y):
    result = np.zeros(shape=(max_y+1, max_x+1))

    for coordinate in coords:
        x1 = coordinate[0][0]
        y1 = coordinate[0][1]
        x2 = coordinate[1][0]
        y2 = coordinate[1][1]

        if x1 == x2 or y1 == y2:
            xrange = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)
            yrange = range(y1, y2+1) if y1 < y2 else range(y2, y1+1)

            for x in xrange:
                for y in yrange:
                    result[y, x] += 1

    return np.count_nonzero(result > 1)

def solve_2(coords, max_x, max_y):
    result = np.zeros(shape=(max_y+1, max_x+1))

    for coordinate in coords:
        x1 = coordinate[0][0]
        y1 = coordinate[0][1]
        x2 = coordinate[1][0]
        y2 = coordinate[1][1]

        if x1 == x2:
            yrange = range(y1, y2+1) if y1 < y2 else range(y2, y1+1)
            for y in yrange:
                result[y, x1] += 1

        elif y1 == y2:
            xrange = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)
            for x in xrange:
                result[y1, x] += 1

        else:
            xbegin = x1 if x1 < x2 else x2
            ybegin = y1 if x1 < x2 else y2
            xend = x2 if x1 < x2 else x1
            yend = y2 if x1 < x2 else y1

            for x in range(xbegin, xend + 1):
                result[ybegin, x] += 1
                if ybegin < yend:
                    ybegin += 1
                elif ybegin > yend:
                    ybegin -= 1

    return np.count_nonzero(result > 1)

(max_x, max_y, coords) = read_input("2021/5/input.txt")
print("Solution 1:", solve_1(coords, max_x, max_y))
print("Solution 2:", solve_2(coords, max_x, max_y))