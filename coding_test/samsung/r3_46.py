from collections import defaultdict, deque
INF = int(1e9)
N = int(input())

start = tuple()
space = []
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 9:
            start = (i, j)
    space.append(data)
space[start[0]][start[1]] = 0

level, count = 2, 0
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

answer = 0
while True:
    x, y = start

    q = deque()
    q.append((x, y))
    dist = [[INF] * N for _ in range(N)]
    dist[x][y] = 0

    # 갈 수 있는 위치 찾기 위해 거리 구하기
    while q:
        nx, ny = q.popleft()
        for d in direction:
            next_x, next_y = nx + d[0], ny + d[1]
            if 0 <= next_x < N and 0 <= next_y < N:
                if dist[next_x][next_y] == INF and space[next_x][next_y] <= level:
                    dist[next_x][next_y] = dist[nx][ny] + 1
                    q.append((next_x, next_y))

    # 가장 가까운 위치 구하기
    mx, my = 0, 0
    min_d = INF
    for i in range(N):
        for j in range(N):
            if dist[i][j] != INF and 0 < space[i][j] < level:
                if dist[i][j] < min_d:  # 순차 탐색하므로, 가장 왼쪽이면서 가장 위쪽 물고기가 자동 선택됨
                    mx, my = i, j
                    min_d = dist[i][j]

    if min_d == INF:  # 갈 곳 없음
        break
    else:
        space[mx][my] = 0  # 물고기 없애고 빈 공간으로 바꾸기
        start = (mx, my)
        answer += min_d
        count += 1
        if count >= level:
            count = 0
            level += 1

print(answer)
