from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < 19 and 0 <= y < 19
direc = [(0, 1), (1, 1), (1, 0), (-1, 1)]


def bfs(x, y):
    q = deque()
    for i in range(4):
        q.append((x, y, i, 1))

    while q:
        qx, qy, dir, cnt = q.popleft()
        if cnt == 5:
            # cnt 6 체크
            nx, ny = qx + direc[dir][0], qy + direc[dir][1]
            if in_range(nx, ny) and board[nx][ny] == board[x][y]:
                continue
            nx, ny = x - direc[dir][0], y - direc[dir][1]
            if in_range(nx, ny) and board[nx][ny] == board[x][y]:
                continue

            # cnt = 5 확실
            print(board[x][y])
            print(x + 1, y + 1)
            sys.exit()

        nx, ny = qx + direc[dir][0], qy + direc[dir][1]
        if in_range(nx, ny) and board[nx][ny] == board[x][y]:
            q.append((nx, ny, dir, cnt + 1))


board = [list(map(int, input().split())) for _ in range(19)]
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            bfs(i, j)

print(0)