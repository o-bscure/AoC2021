import numpy as np
import sys
import matplotlib.pyplot as plt
def main():
    data = [x.strip() for x in open("data13.txt").readlines()]
    coords = []
    folds = []
    array = coords
    for line in data:
        if line == "":
            array = folds
            continue
        array.append(line)
    coords = [x.split(",") for x in coords]
    coords = [(int(y[0]), int(y[1])) for y in coords]
    folds = [x[len("fold along "):].split("=") for x in folds]
    folds = [(x[0],int(x[1])) for x in folds]

    ans = solve(coords, folds)
    plot = []
    for dim in zip(*ans):
        plot.append(dim)
    plt.figure()
    plt.plot(plot[0], plot[1], 'ko')
    plt.show()
    return

def solve(coords, folds):
    for fold in folds:
        new_coords = []
        for coord in coords:
            new_coords.append(flip(coord, fold[0], fold[1]))
        coords = new_coords[:]
    return coords

def flip(coord, axis, index):
    coord_pos = 0 if axis == "x" else 1
    new = list(coord)
    if coord[coord_pos] > index:
        new[coord_pos] = 2*index - coord[coord_pos]
    return tuple(new)

def display(coords):
    max_dims = []
    for dim in zip(*coords):
        max_dims.append(max(dim)+1)
    view = np.zeros(max_dims)
    for x, y in coords:
        view[x,y] = 1
    print(view.T)

if __name__ == "__main__":
    print(main())
