from heapq import heappush, heappop
from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


def find_parent(node):
    if parent[node] == node:
        return node

    parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def bfs(x, y):
    visited[x][y] = True
    graph[x][y] = area_num
    q = deque()
    q.append((x, y))

    while q:
        qx, qy = q.popleft()
        for d in direc:
            nx, ny = qx + d[0], qy + d[1]
            if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = area_num
                q.append((nx, ny))


def find_edges():
    global edges

    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                for d in direc:
                    nx, ny = i + d[0], j + d[1]
                    cnt = 1
                    while in_range(nx, ny) and not graph[nx][ny]:
                        nx, ny = nx + d[0], ny + d[1]
                        cnt += 1
                    if in_range(nx, ny) and graph[nx][ny] != graph[i][j]:
                        if cnt - 1 > 1:
                            heappush(edges, (cnt - 1, graph[i][j], graph[nx][ny]))


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

area_num = 1
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] and not visited[i][j]:
            bfs(i, j)
            area_num += 1

parent = [i for i in range(area_num)]
edges = []
find_edges()

answer = 0
cnt = 0
while edges:
    cost, a, b = heappop(edges)

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += cost
        cnt += 1

if not answer or cnt < area_num - 2:
    print(-1)
else:
    print(answer)