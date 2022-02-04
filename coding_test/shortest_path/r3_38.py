INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if graph[i][j] != INF or graph[j][i] != INF: # i < j 이거나 i > j인 경우 (비교 가능한 경우)
            count += 1
    if count == N: # 모든 수와 비교가 가능하면 답이 될 수 있음
        answer += 1
print(answer)