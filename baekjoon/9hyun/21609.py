from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < N

# 반시계 회전
def rotate():
    global board

    board = list(map(list, zip(*board))) # 행,열 뒤집기
    board.reverse() # 행 뒤집기


def gravity():
    for j in range(N):
        for i in range(N - 2, -1, -1):
            if board[i][j] in [-2, -1]:
                continue

            x, y = i, j
            while x < N - 1:
                x += 1
                if board[x][y] == -2:  # 빈 칸이면
                    board[x - 1][y], board[x][y] = -2, board[x - 1][y]
                else:
                    break


def erase(block):
    score = 0
    for x, y in block[1][0]:
        score += 1
        board[x][y] = -2
    return score ** 2


def search_group():
    groups = dict()
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] not in [-2, -1, 0] and not visited[i][j]:
                visited[i][j] = True
                groups[(i, j)] = [[(i, j)], 0]

                q = deque()
                q.append((i, j))
                rainbow = []
                while q:
                    x, y = q.popleft()
                    for d in direc:
                        nx, ny = x + d[0], y + d[1]
                        if in_range(nx, ny):
                            if not visited[nx][ny] and board[nx][ny] in [0, board[i][j]]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                groups[(i, j)][0].append((nx, ny))
                                if board[nx][ny] == 0:
                                    groups[(i, j)][1] += 1
                                    rainbow.append((nx, ny))
                for rx, ry in rainbow: # 무지개는 중복 포함될 수 있으므로 다시 미방문처리 해줌
                    visited[rx][ry] = False
                if len(groups[(i, j)][0]) == 1:
                    del groups[(i, j)]

    groups = sorted(groups.items(), key=lambda x: (len(x[1][0]), x[1][1], x[0])) # 조건에 맞게 정렬
    if not groups:
        return []
    return groups[-1]


direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

score = 0
while True:
    block = search_group()
    if not block:
        break
    score += erase(block)
    gravity()
    rotate()
    gravity()
print(score)