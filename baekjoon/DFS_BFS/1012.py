from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M

direc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for _ in range(int(input())):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    q = deque()
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    visited = [[False] * M for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visited[i][j]:
                answer += 1
                visited[i][j] = True
                q.append((i, j))
                while q:
                    qx, qy = q.popleft()
                    for d in direc:
                        nx, ny = qx + d[0], qy + d[1]
                        if in_range(nx, ny) and graph[nx][ny] and not visited[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True
    print(answer)