def main():
    data = [list(x.strip()) for x in open("day9.txt").readlines()]
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    ans = solve(data)
    ans.sort()
    top3 = ans[-3:]
    return top3[0]*top3[1]*top3[2]

def solve(array_2d):
    dim1 = len(array_2d)
    dim2 = len(array_2d[0])
    ans = []
    ans_pos = []
    #find all low points
    for i, row in enumerate(array_2d):
        for j, val in enumerate(row):
            greater_than_all = True
            for adj1, adj2  in adjacent(i, j, dim1, dim2):
                greater_than_all = bool(array_2d[adj1][adj2] > val) and greater_than_all
            if greater_than_all:
                ans.append(val)
                ans_pos.append((i,j))


    #flood all low points with BFS, +1 basin size at each step, new basin when queue empty
    basin_sizes = []
    while len(ans_pos) > 0:
        coord = ans_pos.pop(0)
        open_spots = adjacent(coord[0], coord[1], dim1, dim2)
        checked = []
        basin_size = 0
        while len(open_spots) > 0:
            spot = open_spots.pop(0)
            if spot in checked:
                continue
            if array_2d[spot[0]][spot[1]] != 9:
                basin_size += 1
                checked.append(spot)
                for adj in adjacent(spot[0], spot[1], dim1, dim2):
                    if adj not in checked:
                        open_spots.append(adj)
        basin_sizes.append(basin_size)
        new_ans_pos = []
        for p in ans_pos:
            if p not in checked:
                new_ans_pos.append(p)
        ans_pos = new_ans_pos

    return basin_sizes

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
