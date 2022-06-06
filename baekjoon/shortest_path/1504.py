from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijk(start):
    dist = [INF] * (N + 1)
    dist[start] = 0

    q = [(0, start)]
    while q:
        dst, now = heappop(q)

        if dist[now] < dst:
            continue
        for nxt, cost in graph[now]:
            n_dist = dst + cost
            if n_dist < dist[nxt]:
                dist[nxt] = n_dist
                heappush(q, (n_dist, nxt))
    return dist



N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

# v1, v2로 가는 최단 경로 구하기
INF = int(1e9)
dist = dijk(1)

if (dist[v1], dist[v2]) == (INF, INF): # v1, v2 둘다 못 가면 진행할 필요 없음
    print(-1)
else:
    # 1 -> v1 -> v2 -> N vs. 1 -> v2 -> v1 -> N
    dist_v1 = dijk(v1)
    dist_v2 = dijk(v2)

    answer = min(dist[v1] + dist_v1[v2] + dist_v2[N], dist[v2] + dist_v2[v1] + dist_v1[N])
    if answer < INF:
        print(answer)
    else:
        print(-1)