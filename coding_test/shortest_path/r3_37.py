n = int(input())
m = int(input())

graph = [[100001] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c: # 중복되는 간선 중에서 최소값
        graph[a][b] = c

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 100001:
            print('0', end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()