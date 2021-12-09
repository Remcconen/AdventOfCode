import numpy as np

def read_input(file):
    f = open(file, "r")
    return np.array([np.fromiter(line.strip(), dtype=int) for line in f.readlines()])


def solve_1(heatmap):

    low_points = []

    max_i = len(heatmap) - 1
    max_j = len(heatmap[0]) - 1
    for i in range (0, max_i+1):
        for j in range(0, max_j+1):

            adjacent = []

            if (i < max_i):
                adjacent.append(heatmap[i+1, j])
            if (j < max_j):
                adjacent.append(heatmap[i, j+1])
            if (i > 0):
                adjacent.append(heatmap[i-1, j])
            if (j > 0):
                adjacent.append(heatmap[i, j-1])

            if (all(heatmap[i, j] < value for value in adjacent)):
                low_points.append(heatmap[i, j])


    print(low_points)
    risk = sum(low_points) + len(low_points)

    return risk


def find_island(heatmap, visited, i, j):
    if (i < 0 or j < 0 or i >= len(heatmap) or j >= len(heatmap[0]) or visited[i][j] == True or heatmap[i, j] == 9):
        return []

    visited[i, j] = True
    island = [[i, j]]

    c = [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]
    for (x, y) in c:
        newIsland = find_island(heatmap, visited, x, y)
        if (len(newIsland) > 0):
            island = np.concatenate((island, newIsland))

    return island

def solve_2(heatmap):
    islands = []
    visited = np.full((len(heatmap), len(heatmap[0])), False)

    for i in range(0, len(heatmap)):
        for j in range(0, len(heatmap[0])):
            if heatmap[i, j] < 9 and visited[i, j] == False:
                island = find_island(heatmap, visited, i, j)
                islands.append(len(island))

    islands.sort()
    sorted = list(reversed(islands))
    return sorted[0] * sorted[1] * sorted[2]



heatmap = read_input("2021/9/input.txt")

print("Solution 1:", solve_1(heatmap))
print("Solution 2:", solve_2(heatmap))