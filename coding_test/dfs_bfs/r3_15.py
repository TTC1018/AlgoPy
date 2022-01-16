from collections import deque

INF = 1e9

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

distance = [INF] * (N + 1)
distance[X] = 0

q = deque()
q.append(X)
while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == INF:
            distance[next] = distance[now] + 1
            q.append(next)

flag = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        flag = True

if flag == False:
    print(-1)