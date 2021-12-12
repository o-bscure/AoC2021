def main():
    data = [x.strip().split("-") for x in open("data12.txt").readlines()]
    connections = {}
    for c1, c2 in data:
        if c1 not in connections:
            connections[c1] = [c2]
        else:
            connections[c1].append(c2)
        if c2 not in connections:
            connections[c2] = [c1]
        else:
            connections[c2].append(c1)

    ans = solve(connections)

    return ans

def solve(caves):
    paths = 0
    visited = []

    def path_itter(cave):
        nonlocal paths
        if cave == "end":
            paths += 1
            return

        nonlocal visited

        small_cave = cave.islower()
        if small_cave:
            visited.append(cave)
        for neighbor in caves[cave]:
            if neighbor not in visited:
                path_itter(neighbor)
        if small_cave:
            visited.pop()

    path_itter("start")
    return paths



if __name__ == "__main__":
    print(main())
