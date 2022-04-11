from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    graph[u].append(v)
    graph[v].append(u)

answer = 0
for i in range(N):
    if not visited[i]:
        answer += 1
        q = deque()
        q.append(i)
        visited[i] = True
        while q:
            idx = q.popleft()
            for next in [n for n in graph[idx] if not visited[n]]:
                visited[next] = True
                q.append(next)
            graph[idx].clear()
print(answer)