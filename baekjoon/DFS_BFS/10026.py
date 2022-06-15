from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < N


direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
normal = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            q = deque()
            color = graph[i][j]

            normal += 1
            q.append((i, j))
            while q:
                x, y = q.popleft()

                for d in direc:
                    nx, ny = x + d[0], y + d[1]
                    if in_range(nx, ny) and graph[nx][ny] == color:
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

visited = [[False] * N for _ in range(N)]
jnsy = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            q = deque()
            color = [graph[i][j]]
            if color[0] in ['G', 'R']:
                color = ['G', 'R']

            jnsy += 1
            q.append((i, j))
            while q:
                x, y = q.popleft()

                for d in direc:
                    nx, ny = x + d[0], y + d[1]
                    if in_range(nx, ny) and graph[nx][ny] in color:
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

print(normal, jnsy)