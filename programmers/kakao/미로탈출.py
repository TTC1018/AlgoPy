from heapq import heappush, heappop


def solution(n, start, end, roads, traps):
    # 방의 개수 / 출발 방 / 도착 방 / 통로와 이동시간 배열 / 함정 방 번호
    INF = int(1e9)

    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for r in roads:
        P, Q, S = r
        if S < graph[P][Q]:
            graph[P][Q] = S
    for i in range(1, n + 1):
        graph[i][i] = 0

    visited = [[False] * (1 << len(traps)) for _ in range(n + 1)]
    q = [(0, start, 0)]
    while q:
        dist, now, visit = heappop(q)
        if now == end:
            return dist

        if visited[now][visit]:
            continue
        visited[now][visit] = True

        now_is_trapped = False
        trapped_rooms = set()  # 현재 상태에서 발동된 방 저장
        # 발동된 함정 확인
        for i in range(len(traps)): # 발동된 함정 순차 확인
            bit = 1 << i  # 비트마스킹
            if visit & bit:  # 발동된 적 있으면
                if traps[i] == now:
                    visit &= ~bit  # 지금 방이랑 같으면 다시 꺼줘야 됨
                else:
                    trapped_rooms.add(traps[i])
            else: # 발동 안 됐을 때
                if traps[i] == now:
                    visit |= bit  # 지금 방이랑 같으면 켜주기 (지금 도착했으므로)
                    trapped_rooms.add(traps[i])
                    now_is_trapped = True

        # 다음 이동장소 확인
        for nxt in [nxt for nxt in range(1, n + 1) if nxt != now]:
            nxt_is_trapped = True if nxt in trapped_rooms else False
            if now_is_trapped == nxt_is_trapped:  # 둘다 켜져있거나 꺼져있으면 정방향
                if graph[now][nxt] != INF: # 갈 수 있는 곳이면
                    heappush(q, (dist + graph[now][nxt], nxt, visit))
            else: # 한쪽만 활성화 상태면 역방향
                if graph[nxt][now] != INF:
                    heappush(q, (dist + graph[nxt][now], nxt, visit))

    return INF


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
