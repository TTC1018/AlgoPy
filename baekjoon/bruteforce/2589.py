from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            dist = [[-1] * M for _ in range(N)]
            dist[i][j] = 0
            q = deque()
            q.append((i, j))

            while q:
                x, y = q.popleft()

                for d in direc:
                    nx, ny = x + d[0], y + d[1]
                    if in_range(nx, ny) and graph[nx][ny] == 'L':
                        if dist[nx][ny] == -1:
                            dist[nx][ny] = dist[x][y] + 1
                            q.append((nx, ny))
                            answer = max(answer, dist[nx][ny])
print(answer)