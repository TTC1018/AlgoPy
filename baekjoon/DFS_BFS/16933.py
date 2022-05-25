from collections import deque
import sys
in_range = lambda a, b: 0 <= a < N and 0 <= b < M


direc = [(-1, 0), (0, 1), (0, -1), (1, 0)]
N, M, K = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = [[[False] * M for _ in range(N)] for _ in range(K + 1)]

q = deque()
q.append((0, 0, 1, 0, True))
visited[0][0][0] = True
answer = int(1e9)
while q:
    x, y, cnt, b_cnt, daylight = q.popleft()
    if x == N - 1 and y == M - 1:
        answer = min(answer, cnt)
        continue

    for d in direc:
        nx, ny = x + d[0], y + d[1]
        if in_range(nx, ny) and not visited[b_cnt][nx][ny]:
            if not graph[nx][ny]:
                visited[b_cnt][nx][ny] = True
                q.append((nx, ny, cnt + 1, b_cnt, not daylight))
            else:
                if b_cnt + 1 <= K:
                    if daylight:
                        visited[b_cnt][nx][ny] = True
                        q.append((nx, ny, cnt + 1, b_cnt + 1, not daylight))
                    else:
                        q.append((x, y, cnt + 1, b_cnt, not daylight))


if answer == int(1e9):
    print(-1)
else:
    print(answer)