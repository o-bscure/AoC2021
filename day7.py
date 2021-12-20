import numpy as np
def main():
    data = open("data7.txt").readline().split(",")
    data = [int(x) for x in data]
    ans = solve(data)
    return ans

def solve(nums):
    largest = max(nums)
    positions = [0]*(largest+1)
    for i, pos in enumerate(nums):
        for j in range(len(positions)):
            positions[j] += abs(j-pos)
    p = np.array(positions)
    print(np.where(p == min(p)))
    return min(positions)


if __name__ == "__main__":
    print(main())
