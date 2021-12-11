import sys
def main():
    data = open("day10.txt").readlines()
    data = [x.strip() for x in data]
    ans = solve(data)

    score_dict = {  ')': 1, \
                    ']': 2, \
                    '}': 3, \
                    '>': 4 }
    points = []
    for line in ans:
        score = 0
        for c in line:
            score *= 5
            score += score_dict[c]
        points.append(score)

    points.sort()

    return points[len(points)//2]

def solve(lines):
    to_Close = {
            '(': ')', \
            '[': ']', \
            '{': '}', \
            '<': '>', \
            }
    fills = []
    for l, line in enumerate(lines):
        stack = []
        illegal_line = False
        for i, val in enumerate(line):
            if val in to_Close:
                stack.append(to_Close[val])
            elif val is not stack.pop():
                illegal_line = True
                break
        if not illegal_line:
            fills.append(stack[::-1])

    return fills


if __name__ == "__main__":
    print(main())
