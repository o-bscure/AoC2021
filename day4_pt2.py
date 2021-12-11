def main():
    data = open("data4.txt").readlines()
    nums = [int(x) for x in data[0].strip().split(",")]
    raw = data[2:]
    boards = make_boards(raw)
    ans = play(nums, boards)
    return ans

def play(nums, boards):
    state = [[] for _ in boards]
    winners = []
    for n, num in enumerate(nums):
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, value in enumerate(row):
                    if value == num:
                        state[i].append((j, k)) #down, accross
        for l, board_state in enumerate(state):
            for dim in zip(*board_state):
                if (max_count(dim) == 5) and (l not in winners):
                    winners.append(l)
                    if len(winners) == len(boards): #last winner
                        sum_unmarked = count_unmarked(boards[l], board_state)
                        return sum_unmarked*num
    return -1

def count_unmarked(array_2d, marked):
    unmarked_values = []
    for i in range(len(array_2d)):
        for j in range(len(array_2d[i])):
            if (i,j) not in marked:
                value = array_2d[i][j]
                unmarked_values.append(value)
    return sum(unmarked_values)

def max_count(l):
    count = [0]*(max(l)+1)
    for num in l:
        count[num] += 1
    return max(count)


def make_boards(data):
    boards = []
    board = []
    for line in data:
        if line == "\n":
            boards.append(board)
            board = []
        else:
            board.append([x for x in map(int, line.split())])
    return boards


if __name__ == "__main__":
    print(main())
