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
visited[razer[0][0]][razer[0][1]] = -1
for i in range(4):
    x, y = razer[0]
    nx, ny = x + direc[i][0], y + direc[i][1]
    if in_range(nx, ny) and graph[nx][ny] != '*':
        q.append((nx, ny, i))
        visited[nx][ny] = 0


while q:
    x, y, drc = q.popleft()

    if (x, y) == razer[1]:
        continue

    for i in range(4):
        nx, ny = x + direc[i][0], y + direc[i][1]
        if in_range(nx, ny) and graph[nx][ny] != '*':
            if i == drc:
                if visited[x][y] <= visited[nx][ny]:
                    q.append((nx, ny, i))
                    visited[nx][ny] = visited[x][y]
            else:
                if visited[x][y] + 1 <= visited[nx][ny]:
                    q.append((nx, ny, i))
                    visited[nx][ny] = visited[x][y] + 1
print(visited[razer[1][0]][razer[1][1]])
