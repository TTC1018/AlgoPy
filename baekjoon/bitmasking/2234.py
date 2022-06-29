from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < M and 0 <= y < N


def bfs(x, y):
    global cnt

    q = deque()
    q.append((x, y))
    visited[x][y] = True
    area[x][y] = area_num

    c = 1
    while q:
        qx, qy = q.popleft()

        for i in range(4):
            nx, ny = qx + direc[i][0], qy + direc[i][1]
            if in_range(nx, ny) and not (W[qx][qy] & (1 << i)) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                area[nx][ny] = area_num
                c += 1
    cnt.append(c)


N, M = map(int, input().split())
W = [list(map(int, input().split())) for _ in range(M)]
area = [[-1] * N for _ in range(M)]
direc = [(0, -1), (-1, 0), (0, 1), (1, 0)]
area_num = 1

cnt = []
visited = [[False] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            area_num += 1
print(area_num - 1)
print(max(cnt))

# 인접 벽 구하기
near = [set() for _ in range(area_num)]
for i in range(M):
    for j in range(N):
        for d in direc:
            ni, nj = i + d[0], j + d[1]
            if in_range(ni, nj) and area[ni][nj] != area[i][j]:
                near[area[i][j]].add(area[ni][nj])

# 합쳐졌을 때 최대값
sum_val = 0
for i in range(1, area_num):
    for n_num in near[i]:
        sum_val = max(sum_val, cnt[i - 1] + cnt[n_num - 1])
print(sum_val)