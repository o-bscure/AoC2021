def main():
    data = open("data2.txt").readlines()
    data = [x.strip() for x in data]
    a, b = solve(data)
    return a*b

def solve(instructions):
    dist = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        s = instruction.split(" ")
        word = s[0]
        value = int(s[1])
        if word == "down":
            aim += value
        elif word == "up":
            aim -= value
        elif word == "forward":
            dist += value
            depth += aim*value
        else:
            print("OH NOOOO")
    return dist, depth


if __name__ == "__main__":
    print(main())
