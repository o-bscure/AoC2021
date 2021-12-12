def main():
    data = [x.strip().split("-") for x in open("data12.txt").readlines()]
    connections = {}
    for c1, c2 in data:
        if c2 != "start":
            if c1 not in connections:
                connections[c1] = [c2]
            else:
                connections[c1].append(c2)
        if c1 != "start":
            if c2 not in connections:
                connections[c2] = [c1]
            else:
                connections[c2].append(c1)

    ans = solve(connections)

    return ans

def solve(caves):
    path = []
    count = 0
    double_up = False

    def itter(cave):
        nonlocal path
        nonlocal count
        nonlocal double_up
        path.append(cave)
        if cave == 'end':
            count += 1
            path.pop()
            return

        for neighbor in caves[cave]:
            if neighbor.islower() and neighbor in path:
                if not double_up:
                    double_up = True
                    itter(neighbor)
                    double_up = False
            else:
                itter(neighbor)
        path.pop()

    itter('start')
    return count

if __name__ == "__main__":
    print(main())
