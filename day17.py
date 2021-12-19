def main():
    data = open("data17.txt").readline().strip().split(": ")[1].split(", ")
    dims = [tuple(int(y) for y in data[i][2:].split("..")) for i in range(2)]
    return int(solve(dims))

def solve(dims):
    y_initial = (min(dims[1])*-1)-1
    return y_initial*(y_initial+1)/2

if __name__ == "__main__":
    print(main())
