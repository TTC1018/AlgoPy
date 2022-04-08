from collections import deque

INF = int(1e9)
direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
N, M = map(int, input().split())
q = deque()
graph = []
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(M):
        if data[j] == 1:
            q.append(((i, j), 0))
    graph.append(data)


while q:
    s, count = q.popleft()
    x, y = s

    for d in direction:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                graph[nx][ny] = count + 1
                q.append(((nx, ny), count + 1))

result = 0
for i in range(N):
    for j in range(M):
        result = max(result, graph[i][j])
print(result)