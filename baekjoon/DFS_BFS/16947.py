from collections import deque
import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline

q = deque()
def bfs():
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if answer[nxt] == -1:
                answer[nxt] = answer[now] + 1
                q.append(nxt)

def dfs(now, cnt, origin):
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, cnt + 1, origin)
            visited[nxt] = False
        else:
            if cnt > 1 and nxt == origin:
                is_cycle[origin] = True
                return

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

is_cycle = [False] * (N + 1)
visited = [False] * (N + 1)
for num in range(1, N + 1):
    visited[num] = True
    dfs(num, 0, num)
    visited[num] = False

answer = [-1] * (N + 1)
for num in range(1, N + 1):
    if is_cycle[num]:
        answer[num] = 0
        q.append(num)
bfs()
print(*answer[1:])