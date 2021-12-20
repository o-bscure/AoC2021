import sys
def main():
    rules, _, *picture = open("data20.txt").read().split('\n')
    adjacent = {}
    dim1 = len(picture)
    dim2 = len(picture[0])
    for i, row in enumerate(picture):
        for j, char in enumerate(row):
            for ii, jj in adj9(i,j):
                if (ii,jj) not in adjacent:
                    adjacent[(ii,jj)] = 'V'*9
                adjacent[(ii,jj)] = str_insert(adjacent[(ii,jj)], picture[i][j], relation(i,j,ii,jj))
    ans = solve(adjacent, rules)
    return ans

def solve(adjacent, rules):
    void = '.'
    for _ in range(50):
        adj_c = adjacent.copy()
        for node in adjacent:
            adj = adjacent[node]
            new_char = enhance(adj, rules, void)
            i, j = node
            for ii, jj in adj9(i,j):
                if (ii,jj) not in adj_c:
                    adj_c[(ii,jj)] = 'V'*9
                '''
                print("neighbor at ", ii, jj, adj_c[(ii,jj)])
                input()
                print("current node ", i, j, adj)
                input()
                '''
                adj_c[(ii,jj)] = str_insert(adj_c[(ii,jj)], new_char, relation(i,j,ii,jj))
                '''
                print("new at ", ii, jj, adj_c[(ii,jj)])
                input()
                '''
        adjacent = adj_c
        void = '.' if void=='#' else '#'
    count = 0
    for _, string in adjacent.items():
        if string[4] == "#":
            count+=1
    return count

def enhance(string, rules, void):
    return rules[int(string.replace("V",void).replace(".","0").replace("#","1"), 2)]

def adj9(i,j):
    return [(i,j),(i+1,j),(i-1,j),(i+1,j+1),(i,j+1),(i,j-1),(i-1,j-1),(i-1,j+1),(i+1,j-1)]

def str_insert(string, char, index):
    return string[:index] + char + string[index+1:]


def relation(to_i, to_j, from_i, from_j):
    d = {(-1,-1): 0,
         (-1, 0): 1,
         (-1, 1): 2,
         ( 0,-1): 3,
         ( 0, 0): 4,
         ( 0, 1): 5,
         ( 1,-1): 6,
         ( 1, 0): 7,
         ( 1, 1): 8}
    i_offset = to_i - from_i
    j_offset = to_j - from_j
    return d[(i_offset,j_offset)]


if __name__ == "__main__":
    print(main())
