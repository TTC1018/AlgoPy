from collections import deque
import sys
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


INF = int(1e9)
direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

q = deque()
q.append(((0, 0), 1, False))
visited[0][0] = [True, False]
answer = INF
while q:
    pos, dist, breaked = q.popleft()
    x, y = pos
    if pos == (N - 1, M - 1):
        answer = min(answer, dist)
        continue

    for d in direc:
        nx, ny = x + d[0], y + d[1]
        if in_range(nx, ny):
            if not visited[nx][ny][breaked]:
                if graph[nx][ny] == 0:
                    q.append(((nx, ny), dist + 1, breaked))
                    visited[nx][ny][breaked] = True
                elif not breaked:
                    q.append(((nx, ny), dist + 1, True))
                    visited[nx][ny][breaked] = True


if answer != INF:
    print(answer)
else:
    print(-1)