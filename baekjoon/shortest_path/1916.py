import heapq


INF = int(1e9)
N, M = int(input()), int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s_num, e_num, cost = map(int, input().split())
    graph[s_num].append((e_num, cost))
    
start, end = map(int, input().split())
distance = [INF] * (N + 1)
distance[start] = 0

# 다익스트라
q = [(0, start)]
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for next, cost in graph[now]:
        n_dist = dist + cost
        if n_dist < distance[next]:
            distance[next] = n_dist
            heapq.heappush(q, (n_dist, next))
print(distance[end])