import sys
input = sys.stdin.readline


def dfs(x, y):
    global answer

    direc = graph[x][y]
    nx, ny = x + d[direc][0], y + d[direc][1]

    if not visited[nx][ny]: # 배정 안 된 지역
        visited[nx][ny] = area_idx
        dfs(nx, ny)
    elif visited[nx][ny] == area_idx: # 싸이클이면
        answer += 1


N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
d = {'N': (-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}
visited = [[0] * M for _ in range(N)]


area_idx = 0
answer = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            area_idx += 1
            visited[i][j] = area_idx
            dfs(i, j)
print(answer)