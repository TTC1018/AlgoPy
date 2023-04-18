from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

q = deque([(0, 0, 0, False)]) # x, y, 시간, 그람유무
visited[0][0][0] = 1

while q:
    x, y, t, g = q.popleft()
    if x == N - 1 and y == M - 1:
        print(t)
        break

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and t + 1 <= T:
            if g:
                if not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    q.append((nx, ny, t + 1, g))
            else:
                if not visited[nx][ny][0] and board[nx][ny] != 1:
                    visited[nx][ny][0] = True
                    if board[nx][ny] == 0:
                        q.append((nx, ny, t + 1, g))
                    elif board[nx][ny] == 2:
                        q.append((nx, ny, t + 1, True))
else:
    print('Fail')