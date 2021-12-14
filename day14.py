import sys
def main():
    data = [x.strip() for x in open("data14.txt").readlines()]
    seed = data[0]
    rules = {}
    for line in data[2:]:
        s = line.split(" -> ")
        rules[s[0]] = s[1]
    pairs = {}
    for pair in rules:
        pairs[pair] = 0
    for i in range(len(seed)-1):
        pair = seed[i:i+2]
        pairs[pair] += 1
    count = {}
    for r in rules:
        count[rules[r]] = seed.count(rules[r])

    ans = solve(rules, pairs, count)
    vals = [ans[k] for k in ans]

    return max(vals) - min(vals)

def solve(rules, pairs, count):
    steps = 10

    for _ in range(steps):
        new = {}
        for k in pairs:
            new[k] = 0
        for target in rules:
            insertion = rules[target]
            count[insertion] += pairs[target]
            new[target] += -1*pairs[target]
            for new_pair in [target[0]+insertion, insertion+target[1]]:
                new[new_pair] += pairs[target]
        for k in new:
            pairs[k] += new[k]

    return count



if __name__ == "__main__":
    print(main())
