from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < H and 0 <= y < W
INF = int(1e9)
direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
W, H = map(int, input().split())
graph = []
razer = []
for i in range(H):
    data = list(input().rstrip())
    for j in range(W):
        if data[j] == 'C':
            razer.append((i, j))
    graph.append(data)

q = deque()
visited = [[INF for _ in range(W)] for _ in range(H)]
for i in range(4):
    x, y = razer[0]
    nx, ny = x + direc[i][0], y + direc[i][1]
    if in_range(nx, ny) and graph[nx][ny] != '*':
        q.append((nx, ny, 0, i))
        visited[nx][ny] = 0

answer = INF
while q:
    x, y, cnt, drc = q.popleft()

    if (x, y) == razer[1]:
        answer = min(answer, cnt)
        continue

    for i in range(4):
        nx, ny = x + direc[i][0], y + direc[i][1]
        if in_range(nx, ny) and graph[nx][ny] != '*':
            if i == drc and cnt <= visited[nx][ny]:
                q.append((nx, ny, cnt, i))
                visited[nx][ny] = cnt
            else:
                if cnt + 1 <= visited[nx][ny]:
                    q.append((nx, ny, cnt + 1, i))
                    visited[nx][ny] = cnt + 1
print(answer)