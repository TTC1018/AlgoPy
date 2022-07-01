from heapq import heappush, heappop
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < N


INF = int(1e9)
direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
case = 1
while True:
    N = int(input())
    if not N:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    dist = [INF] * (N * N)
    dist[0] = graph[0][0]


    q = [(dist[0], 0, 0)]
    while q:
        cost, x, y = heappop(q)
        if x == N - 1 and y == N - 1:
            print('Problem {}: {}'.format(case, dist[N * N - 1]))
            break

        if dist[x * N + y] < cost:
            continue

        for d in direc:
            nx, ny = x + d[0], y + d[1]
            if in_range(nx, ny):
                n_cost = cost + graph[nx][ny]
                if n_cost < dist[nx * N + ny]:
                    dist[nx * N + ny] = n_cost
                    heappush(q, (n_cost, nx, ny))
    case += 1