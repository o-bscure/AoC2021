def main():
    data = open("data6.txt").readline().split(",")
    data = [int(x) for x in data]
    days = 256
    spawns = [0 for _ in range(days)]
    for n in data:
        pos = 0
        while n+pos < len(spawns):
            spawns[n+pos] += 1
            pos += 7
    for d in range(days):
        num_of_spawns = spawns[d]
        pos = 9
        while d+pos < len(spawns):
            spawns[d+pos] += num_of_spawns
            pos += 7
    return sum(spawns) + len(data)


if __name__ == "__main__":
    print(main())
