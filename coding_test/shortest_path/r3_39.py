import heapq

INF = int(1e9)

T = int(input())
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for _ in range(T):
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    q = [(space[0][0], 0, 0)]
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for d in direction:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N: # 가능 범위 내
                next_dist = dist + space[nx][ny] # 다음 지점까지 소요되는 거리
                if next_dist < distance[nx][ny]: # 기록된 최단 거리보다 짧을 때
                    distance[nx][ny] = next_dist # 최단 거리 갱신
                    heapq.heappush(q, (next_dist, nx, ny)) # heapq에 삽입

    print(distance[N - 1][N - 1])