import sys
input = sys.stdin.readline

INF = int(1e9)
n, k = map(int, input().split())

graph = [[INF] * n for _ in range(n)]
for _ in range(k):
    c1, c2 = map(int, input().split()) # c1 > c2
    graph[c2 - 1][c1 - 1] = 1
for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = []
s = int(input())
for _ in range(s):
    c1, c2 = map(int, input().split())
    c1, c2 = c1 - 1, c2 - 1
    if graph[c2][c1] != INF and graph[c1][c2] == INF:
        print(-1)
    elif graph[c1][c2] != INF and graph[c2][c1] == INF:
        print(1)
    else:
        print(0)