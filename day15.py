import sys
import heapq as q
import numpy as np
def main():
    data = np.array([ list(int(y) for y in x.strip()) for x in open("data15.txt").readlines()])
    ans = solve(data)
    return ans

def solve(array_2d):
    queue = []
    dim1, dim2 = np.shape(array_2d)
    processed = {}
    dist = []
    for i in range(len(array_2d)):
        t = []
        for j in range(len(array_2d[i])):
            t.append(np.inf)
            processed[(i,j)] = False
        dist.append(t)
    dist = np.array(dist)
    dist[0,0] = 0
    q.heappush(queue, (dist[0,0], (0,0))) #heap object is (distance, (i, j))
    while queue != []:
        coord = q.heappop(queue)[1]
        if processed[coord]:
            continue
        processed[coord] = True
        i = coord[0]
        j = coord[1]
        for ii, jj in adj(i,j,dim1,dim2):
            next_coord = (ii, jj)
            weight = array_2d[ii, jj]
            if dist[i,j]+weight < dist[ii,jj]:
                dist[ii,jj] = dist[i,j]+weight
                q.heappush(queue, (dist[ii,jj], next_coord))
    return dist

def adj(i,j,dim1,dim2):
    [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
    ans = []
    if i > 0:
        ans.append((i-1, j))
    if i < dim1-1:
        ans.append((i+1, j))
    if j > 0:
        ans.append((i, j-1))
    if j < dim2-1:
        ans.append((i, j+1))
    return ans



if __name__ == "__main__":
    print(main())
