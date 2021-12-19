def main():
    data = open("data17.txt").readline().strip().split(": ")[1].split(", ")
    dims = [tuple(int(y) for y in data[i][2:].split("..")) for i in range(2)]
    return solve(dims)

def solve(dims):
    y_min = min(dims[1])
    y_max = (y_min*-1)-1
    y_vels = []
    for v in range(y_max, y_min-1, -1):
        if v > 0:
            vel = (v*-1)-1
        else:
            vel = v
        pos = 0
        while pos >= y_min:
            if pos <= max(dims[1]):
                y_vels.append(v)
                break
            pos += vel
            vel -= 1

    x_vels = []
    v = 0
    while v <= max(dims[0]):
        pos = 0
        vel = v
        while vel >= 0 and pos <= max(dims[0]):
            if pos >= min(dims[0]):
                x_vels.append(v)
                break
            pos += vel
            vel -= 1
        v += 1

    count = 0
    for xv in x_vels:
        for yv in y_vels:
            x_pos = y_pos = 0
            xv_ = xv
            yv_ = yv
            while x_pos <= max(dims[0]) and y_pos >= min(dims[1]):
                if x_pos >= min(dims[0]) and y_pos <= max(dims[1]):
                    count += 1
                    break
                x_pos += xv_
                y_pos += yv_
                yv_ -= 1
                if xv_ != 0:
                    xv_ -= 1

    return count

if __name__ == "__main__":
    print(main())
