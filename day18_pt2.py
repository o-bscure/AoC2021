import math
def main():
    data = [x.strip() for x in open("data18.txt").readlines()]
    largest = 0
    for i, d1 in enumerate(data):
        for j, d2 in enumerate(data):
            if j != i:
                ans = solve([d1, d2])
                ans = rsum(ans)
                largest = max(largest, ans)
    return largest

def rsum(x):
    if len(x) == 1:
        return int(x)

    x = x[1:-1]
    i = 0
    level = 0
    while i < len(x):
        if x[i]=='[':
            level += 1
        elif x[i]==']':
            level -= 1
        elif x[i]==',' and level==0:
            break
        i += 1
    return rsum(x[:i])*3 + rsum(x[i+1:])*2


def solve(nums):
    current = simplify(nums[0])
    for num in nums[1:]:
        current = "[{},{}]".format(current, num)
        current = simplify(current)
    return current

def simplify(num):
    while True:
        num, exploded = check_explode(num)
        if exploded:
            continue
        num, splitted = check_split(num)
        if splitted:
            continue
        return num

def check_split(num):
    i = 0
    num_digit_range = []
    while i < len(num)-1:
        if num[i].isnumeric() and num[i+1].isnumeric():
            j = i
            while j < len(num)-1 and num[j].isnumeric():
                j += 1
            num_digit_range = [i,j]
            break
        i += 1
    if num_digit_range == []:
        return num, False
    else:
        left_side = num[:num_digit_range[0]]
        right_side = num[num_digit_range[1]:]
        m = int(num[num_digit_range[0]:num_digit_range[1]])
        return left_side + '[{},{}]'.format(math.floor(m/2), math.ceil(m/2)) + right_side, True


def check_explode(num):
    layer = 0
    exploded = False
    num_new = num[:]
    for i, c in enumerate(num):
        if c == ',':
            continue
        if c == '[':
            if layer == 4:
                index1 = index2 = i
                while num[index2] != ']':
                    index2 += 1
                j = index2
                num_l, num_r = num[i+1:j].split(",")
                left_num_range = []
                in_num = False
                while index1 >= 0:
                    if num[index1].isnumeric() and not in_num:
                        left_num_range.append(index1+1)
                        in_num = True
                    elif (not num[index1].isnumeric()) and in_num:
                        left_num_range.append(index1+1)
                        break
                    index1 -= 1
                right_num_range = []
                in_num = False
                while index2 < len(num):
                    if num[index2].isnumeric() and not in_num:
                        right_num_range.append(index2)
                        in_num = True
                    elif (not num[index2].isnumeric()) and in_num:
                        right_num_range.append(index2)
                        break
                    index2 += 1
                left_part = num[:i]
                right_part = num[j+1:]
                if left_num_range != []:
                    left_num_range = left_num_range[::-1]
                    left_part = left_part[:left_num_range[0]] + \
                                str(int(left_part[left_num_range[0]:left_num_range[1]])+int(num_l)) + \
                                left_part[left_num_range[1]:]
                if right_num_range != []:
                    right_part = right_part[:right_num_range[0]-j-1] + \
                                str(int(right_part[right_num_range[0]-j-1:right_num_range[1]-j-1])+int(num_r)) + \
                                right_part[right_num_range[1]-j-1:]
                return left_part + "0" + right_part, True
            else:
                layer += 1
                continue
        if c == ']':
            layer -= 1
            continue
    return num, False


if __name__ == "__main__":
    print(main())
