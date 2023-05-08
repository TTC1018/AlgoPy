from collections import deque
import sys
input = sys.stdin.readline
d = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def bfs(i, j):
    visited[i][j] = True
    q = deque([(i, j)])

    s, w = 0, 0
    if B[i][j] == 'o':
        s += 1
    elif B[i][j] == 'v':
        w += 1

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if B[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if B[nx][ny] == 'o':
                        s += 1
                    elif B[nx][ny] == 'v':
                        w += 1
                    q.append((nx, ny))

    if s > w:
        return s, 0
    else:
        return 0, w


R, C = map(int, input().split())
B = [input().rstrip() for _ in range(R)]
visited = [[False] * C for _ in range(R)]

a1, a2 = 0, 0
for i in range(R):
    for j in range(C):
        if B[i][j] != '#' and not visited[i][j]:
            s, w = bfs(i, j)
            a1 += s
            a2 += w
print(a1, a2)
