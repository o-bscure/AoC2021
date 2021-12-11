import numpy as np
import sys
import seaborn
import matplotlib.pyplot as plt

def main():
    data = open("data5.txt").readlines()
    data = [parse(x.strip()) for x in data]
    grid = points(data)
    count = 0
    for row in grid:
        for val in row:
            if val >= 2:
                count += 1
    plt.figure(figsize=(10,10))
    a = np.array(grid)
    ax = seaborn.heatmap(a, cbar=None, xticklabels=False, yticklabels=False)
    plt.savefig("vents_day5.png", bbox_inches='tight', dpi=1000)
    return count

def points(point_pairs):
    grid = [[0]*1000 for _ in range(1000)]
    for p, pairs in enumerate(point_pairs):
        dims = list(zip(*pairs))
        for d, dim in enumerate(dims):
            if dim[0] == dim[1]:
                if d == 0:
                    new_points = [(dim[0], x) for x in range(min(dims[1]), max(dims[1])+1)]
                elif d ==1:
                    new_points = [(y, dim[0]) for y in range(min(dims[0]), max(dims[0])+1)]
                else:
                    print("OHN OOOOOOOOOOOOO")
                '''
                print("pairs: ", pairs, "\n"\
                      "points to add: ", new_points, "\n"\
                      "points so far: ", points_final, "\n"\
                      )
                input()
                '''
                for i, j in new_points:
                    grid[i][j] += 1
                break
    return grid




def parse(line):
    coords = line.split(" -> ")
    coords = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in coords]
    return coords

if __name__ == "__main__":
    print(main())
