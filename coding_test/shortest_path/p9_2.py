INF = int(1e9)
N, M = map(int, input().split())

graph = [[INF] * N for _ in range(N)]
for i in range(N):
    graph[i - 1][i - 1] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1], graph[b - 1][a - 1] = 1, 1

X, K = map(int, input().split())

for i in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])


answer = graph[0][K - 1] + graph[K - 1][X - 1]
if answer >= INF:
    print(-1)
else:
    print(answer)