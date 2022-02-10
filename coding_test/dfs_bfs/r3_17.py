from collections import deque

N, K = map(int, input().split())
q = deque()

graph = []
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] != 0:
            q.append((data[j], i, j))
    graph.append(data)

S, X, Y = map(int, input().split())
q = deque(sorted(q, key=lambda x:x[0]))

direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
second, t_sec = 0, len(q)
while q:
    if second == S:
        break

    virus, x, y = q.popleft()
    for d in direc:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, nx, ny))
    t_sec -= 1

    if t_sec == 0:
        second += 1
        t_sec = len(q)

print(graph[X - 1][Y - 1])