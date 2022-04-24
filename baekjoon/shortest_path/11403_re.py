import sys
input =  sys.stdin.readline


INF = int(1e9)
N = int(input())
graph = [[INF] * N for _ in range(N)]
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 1:
            graph[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] != INF:
            answer[i][j] = 1

for a in answer:
    print(*a)