from collections import deque
import sys
input = sys.stdin.readline


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
answer = []
visited = [False] * (N + 1)

q = deque()
q.append((X, 0))
visited[X] = True

while q:
    now, dist = q.popleft()
    if dist == K:
        answer.append(now)

    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, dist + 1))

answer.sort()
if len(answer) > 0:
    for a in answer:
        print(a)
else:
    print(-1)