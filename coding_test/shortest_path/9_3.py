INF = int(1e9)

N = int(input())
M = int(input())

graph = [[INF] * (N + 1) for _ in range(N + 1)] # 노드 간의 거리를 저장하는 그래프

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0 # 자신에게 가는 경로는 다 0으로 초기화

for _ in range(M):
    a, b, c = map(int, input().split()) # 노드 간 거리 입력 받아 graph 초기화
    graph[a][b] = c

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # a -> b 보다 a -> k -> b가 더 짧은지를 확인

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if graph[a][b] == INF:
            print("INFINITY", end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()