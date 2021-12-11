def main():
    data = open("day10.txt").readlines()
    data = [x.strip() for x in data]
    ans = solve(data)

    score_dict = {  ')': 3, \
                    ']': 57, \
                    '}': 1197, \
                    '>': 25137 }
    score = 0
    for c in ans:
        score += score_dict[c]

    return score

def solve(lines):
    to_Close = {'(': ')', \
                '[': ']', \
                '{': '}', \
                '<': '>'}
    illegal_chars = []
    for line in lines:
        stack = []
        for i, val in enumerate(line):
            if val in to_Close:
                stack.append(to_Close[val])
            elif val is not stack.pop():
                illegal_chars.append(val)

    return illegal_chars


if __name__ == "__main__":
    print(main())
