import math

def main():
    data = open("data1.txt").readlines()
    data = [int(x.strip()) for x in data]
    print(solve(data))
    return

def solve(data):
    count = 0
    prev_num = math.inf
    for n in range(0, len(data)-1):
        next_num = data[n]
        if next_num > prev_num:
            count += 1
        prev_num = next_num
    return count

if __name__ == "__main__":
    main()
