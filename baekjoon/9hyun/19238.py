from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < N


def drive():
    global R, C, fuel

    visited = [[False] * N for _ in range(N)]
    visited[R][C] = True
    q = deque()
    q.append((R, C, 0))

    cand = []
    if (R, C) in c_start: # 현재 지점에 승객 있으면
        cand.append((R, C, 0))
    else:
        while q:
            x, y, dist = q.popleft()
            for d in direc:
                nx, ny = x + d[0], y + d[1]
                if in_range(nx, ny) and not graph[nx][ny]:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        if (nx, ny) in c_start:
                            cand.append((nx, ny, dist + 1))
                            continue
                        else:
                            if dist + 1 <= fuel:
                                q.append((nx, ny, dist + 1))
    # 갈 곳 없으면
    if len(cand) == 0:
        print(-1)
        sys.exit()

    # 최단거리, 행, 열 순으로 정렬
    cand.sort(key=lambda x:(x[2], x[0], x[1]))
    c_num = c_start.index((cand[0][0], cand[0][1]))
    needed_f = cand[0][2] # 픽업까지 필요한 연료
    sx, sy = c_start[c_num]
    dx, dy = c_end[c_num]

    fuel -= needed_f
    if fuel <= 0: # 픽업 불가한 경우
        print(-1)
        sys.exit()
    else:
        R, C = sx, sy
        visited = [[False] * N for _ in range(N)]
        visited[R][C] = True
        q = deque()
        q.append((R, C, 0))

        # 도착지점 최단거리 찾기
        while q:
            x, y, dist = q.popleft()

            if (x, y) == (dx, dy):
                fuel -= dist
                if fuel < 0:
                    print(-1)
                    sys.exit()
                else:
                    fuel += dist * 2
                    R, C = dx, dy
                break

            for d in direc:
                nx, ny = x + d[0], y + d[1]
                if in_range(nx, ny) and not graph[nx][ny]:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, dist + 1))

        if (R, C) == (sx, sy): # 도착지에 도달 불가능 할 때
            print(-1)
            sys.exit()

    del c_start[c_num]
    del c_end[c_num]


direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M, fuel = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
R, C = map(int, input().split())
R, C = R - 1, C - 1

c_start = []
c_end = []
for i in range(M):
    sx, sy, dx, dy = map(int, input().split())
    c_start.append((sx - 1, sy - 1))
    c_end.append((dx - 1, dy - 1))

for _ in range(M):
    drive()
print(fuel)