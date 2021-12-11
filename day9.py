def main():
    data = [list(x.strip()) for x in open("data9.txt").readlines()]
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    ans = solve(data)
    return sum(ans) + len(ans)

def solve(array_2d):
    dim1 = len(array_2d)
    dim2 = len(array_2d[0])
    ans = []
    ans_pos = []
    for i, row in enumerate(array_2d):
        for j, val in enumerate(row):
            greater_than_all = True
            for adj1, adj2  in adjacent(i, j, dim1, dim2):
                greater_than_all = bool(array_2d[adj1][adj2] > val) and greater_than_all
            if greater_than_all:
                ans.append(val)
                ans_pos.append((i,j))
    return ans

def adjacent(i1, i2, len1, len2):
    options = [(i1+1, i2), (i1-1, i2), (i1, i2+1), (i1, i2-1)]
    ans = []
    for i, j in options:
        if (i<0) or (i>=len1) or (j<0) or (j>=len2):
            continue
        ans.append((i,j))
    return ans

if __name__ == "__main__":
    print(main())
