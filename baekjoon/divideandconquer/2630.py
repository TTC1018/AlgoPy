import sys
input = sys.stdin.readline


def check(x, y, size):
    start = board[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] != start:
                return False
    return True


def recur(x, y, size):
    global answers

    if size == 1:
        answers[board[x][y]] += 1
        return

    if check(x, y, size):
        answers[board[x][y]] += 1
    else:
        for i in range(x, x + size, size // 2):
            for j in range(y, y + size, size // 2):
                recur(i, j, size // 2)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answers = [0, 0]
recur(0, 0, n)
print('\n'.join(map(str, answers)), end='')
