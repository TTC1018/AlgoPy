from heapq import heappush, heappop
from copy import deepcopy


def solution(n, start, end, roads, traps):
    # 방의 개수 / 출발 방 / 도착 방 / 통로와 이동시간 배열 / 함정 방 번호
    INF = int(1e9)

    graph = [[] for _ in range(n + 1)]
    for r in roads:
        P, Q, S = r
        graph[P].append((Q, S, True))
        graph[Q].append((P, S, False))

    q = [(0, start, deepcopy(graph))]
    distance = [INF] * (n + 1)
    distance[start] = 0
    while q:
        dist, now, now_graph = heappop(q)
        if distance[now] < dist:
            continue
        if now == end:
            continue
        if now in traps:
            for nxt, cst, can in now_graph[now]:
                now_graph[nxt].remove((now, cst, not can))
                now_graph[nxt].append((now, cst, can))
            n_len = len(now_graph[now])
            for i in range(n_len):
                nxt, cst, can = now_graph[now][i]
                now_graph[now][i] = (nxt, cst, not can)
        for nxt, cst, can in now_graph[now]:
            if can:
                n_dist = dist + cst
                if n_dist < distance[nxt]:
                    distance[nxt] = n_dist
                    heappush(q, (n_dist, nxt, deepcopy(now_graph)))


    return distance[end]


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
