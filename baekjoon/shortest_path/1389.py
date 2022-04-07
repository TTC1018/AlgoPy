INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * N for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A][B] = 1
    graph[B][A] = 1
for i in range(N):
    graph[i][i] = 0


for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = -1
temp_sum = INF
for i in range(N):
    now_sum = sum(graph[i])
    if temp_sum > now_sum:
        answer = i
        temp_sum = now_sum
print(answer + 1)