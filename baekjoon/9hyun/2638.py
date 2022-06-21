from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


direc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    area[x][y] = 0

    while q:
        i, j = q.popleft()

        for d in direc:
            ni, nj = i + d[0], j + d[1]
            if in_range(ni, nj) and not graph[ni][nj]:
                if area[ni][nj] == -1:
                    area[ni][nj] = 0
                    q.append((ni, nj))


def detecting(x, y):
    cnt = 0
    for d in direc:
        nx, ny = x + d[0], y + d[1]
        if in_range(nx, ny) and not area[nx][ny]:
            cnt += 1

    if cnt >= 2:
        return True
    return False


def is_finished():
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                return False
    return True


INF = int(1e9)
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


time = 0
while True:
    time += 1
    area = [[-1] * M for _ in range(N)]
    bfs(0 ,0)

    # 녹을 치즈 찾기
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if detecting(i, j):
                    area[i][j] = 1

    # 치즈 없애기
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1:
                graph[i][j] = 0

    if is_finished():
        break
print(time)