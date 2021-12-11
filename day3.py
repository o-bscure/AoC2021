def main():
    data = open("data3.txt").readlines()
    data = [x.strip() for x in data]
    n = solve(data)
    return n

def solve(nums):
    dim1 = len(nums)
    dim2 = len(nums[1])
    ones = [0]*dim2
    for num in nums:
        for i in range(len(num)):
            print("ones: ", ones, "next index: ", i, "num: ", num)
            ones[i] += int(num[i])
    ans = ""
    ans2 = ""
    for j in range(len(ones)):
        if ones[j] > dim1//2:
            ans += "1"
            ans2 += "0"
        else:
            ans += "0"
            ans2 += "1"


    return int(ans, base=2)*int(ans2, base=2)




if __name__ == "__main__":
    print(main())
