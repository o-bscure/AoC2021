import sys
def main():
    data = [x.strip().split(" | ")[1].split(" ") for x in open("data8.txt").readlines()]
    count = []
    for row in data:
        for string in row:
            count.append(len(string))
    print(count, len(count))
    c = 0
    for n in count:
        if (n==2) or (n==4) or (n==3) or (n==7):
            c += 1
    return c

if __name__ == "__main__":
    print(main())
