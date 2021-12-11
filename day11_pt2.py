import numpy as np
import sys

def main():
    data = open("data11.txt").readlines()
    data = np.array([[int(xx) for xx in x.strip()] for x in data])
    ans = solve(data)
    return ans

def solve(nparray):
    all_same = lambda array: np.all(array==array[0,0])
    dim1, dim2 = np.shape(nparray)

    def itter(i, j):
        val = nparray[i,j]
        if val >= 10:
            nparray[i,j] = -1
            for n1, n2 in neighbor_coords(i, j, dim1, dim2):
                if nparray[n1, n2] != -1:
                    nparray[n1,n2] += 1
                    itter(n1, n2)

    step = 0
    while not all_same(nparray):
        step += 1
        nparray += 1
        for i in range(dim1):
            for j in range(dim2):
                itter(i,j)
        nparray[nparray == -1] = 0

    return step

def neighbor_coords(i1, i2, len1, len2):
    options = [(i1+1, i2), (i1-1, i2), (i1, i2+1), (i1, i2-1), \
               (i1+1, i2+1), (i1-1, i2-1), (i1-1, i2+1), (i1+1, i2-1)]
    ans = []
    for i, j in options:
        if (i<0) or (i>=len1) or (j<0) or (j>=len2):
            continue
        ans.append((i,j))
    return ans

if __name__ == "__main__":
    print(main())
