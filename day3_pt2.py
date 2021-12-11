def main():
    data = open("data3.txt").readlines()
    data = [x.strip() for x in data]
    o2 = solve(data, most_common)
    co2 = solve(data, least_common)
    return int(o2, base=2)*int(co2, base=2)

def solve(nums, selector):
    options = list(range(len(nums)))
    pos = 0
    while len(options) > 1:
        target_val = selector(nums, options, pos)
        new_options = []
        for index in options:
            if nums[index][pos] == target_val:
                new_options.append(index)
        print("postion: ", pos, "target value: ", target_val, "\n",\
              "chosen/index/values left: \n",\
              "ref: \t\t", "".join([str(x) for x in range(1, 10)]), "\n",\
              "\n".join([str((i in new_options, i))+"\t"+v for i, v in \
                         zip(options, [nums[x] for x in options])])\
              )
        input()
        options = new_options
        pos += 1
    ans = nums[options[0]]
    print("winner! ~ ", ans)
    input()
    return ans

def most_common(nums, indicies, pos):
    options_list = [nums[i] for i in indicies]
    columns = list(zip(*options_list))
    column = [int(x) for x in columns[pos]]
    if sum(column) >= len(column)/2:
        return "1"
    else:
        return "0"

def least_common(nums, indicies, pos):
    options_list = [nums[i] for i in indicies]
    columns = list(zip(*options_list))
    column = [int(x) for x in columns[pos]]
    if (sum(column) >= len(column)/2) and (sum(column) != len(column)):
        return "0"
    else:
        return "1"


if __name__ == "__main__":
    print(main())
