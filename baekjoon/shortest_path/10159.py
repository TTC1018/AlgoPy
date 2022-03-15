import sys
input = sys.stdin.readline


INF = int(1e9)
N = int(input())
M = int(input())

graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0

for i in range(M): # 무게: 앞 > 뒤
    a, b = map(int, input().split())
    graph[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


answer, total = [] , N - 1
for i in range(1, N + 1):
    count = 0
    for j in [num for num in range(1, N + 1) if num != i]:
        if graph[j][i] == INF and graph[i][j] == INF:
            count += 1
    answer.append(count)

for a in answer:
    print(a)