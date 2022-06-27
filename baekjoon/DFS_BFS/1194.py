from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


N, M = map(int, input().split())
graph = []
sx, sy = None, None
for i in range(N):
    data = list(input().rstrip())
    if not sx:
        for j in range(M):
            if data[j] == '0':
                sx, sy = i, j
                data[j] = '.'
                break
    graph.append(data)


visited = [[[False] * (1 << 7 - 1) for _ in range(M)] for _ in range(N)]
q = deque()
q.append((sx, sy, 0, 0))
key = {chr(alpha): (1 << (alpha - ord('a'))) for alpha in range(ord('a'), ord('f') + 1)}
direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = int(1e9)
while q:
    x, y, cnt, mask = q.popleft()
    if graph[x][y] == '1':
        answer = cnt
        break

    for d in direc:
        nx, ny = x + d[0], y + d[1]
        if in_range(nx, ny) and not visited[nx][ny][mask]:
            if graph[nx][ny].isalpha():
                if graph[nx][ny].isupper():
                    if key[graph[nx][ny].lower()] & mask:
                        q.append((nx, ny, cnt + 1, mask))
                        visited[nx][ny][mask] = True
                else:
                    q.append((nx, ny, cnt + 1, mask | key[graph[nx][ny]]))
                    visited[nx][ny][mask] = True
            elif graph[nx][ny] == '.':
                q.append((nx, ny, cnt + 1, mask))
                visited[nx][ny][mask] = True
            elif graph[nx][ny] == '1':
                q.append((nx, ny, cnt + 1, mask))

if answer == int(1e9):
    print(-1)
else:
    print(answer)