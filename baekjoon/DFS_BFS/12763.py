import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(node, t, c):
    global answer

    if node == N - 1:
        answer = min(answer, c)
        return

    for nxt, time, cost in graph[node]:
        if not visited[nxt]:
            if t + time <= T and c + cost <= M:
                visited[nxt] = True
                dfs(nxt, t + time, c + cost)
                visited[nxt] = False


N = int(input())
T, M = map(int, input().split())
L = int(input())

INF = int(1e9)
graph = [[] for _ in range(N)]

for _ in range(L):
    a, b, time, cost = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, time, cost))
    graph[b].append((a, time, cost))


answer = INF
visited = [False] * N
visited[0] = True
dfs(0, 0, 0)
if answer == INF:
    print(-1)
else:
    print(answer)