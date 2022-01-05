from collections import deque

N, M = map(int, input().split())
m = []
for i in range(N):
    m.append(list(map(int, input())))


direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[0] * M for i in range(N)]

q = deque()
q.append((0, 0))
visited[0][0] = 1

while q:
    x, y = q.popleft()

    for d in direc:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx < N and 0 <= ny < M:
            if m[nx][ny] != 0 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                m[nx][ny] = m[x][y] + 1

print(m[N-1][M-1])