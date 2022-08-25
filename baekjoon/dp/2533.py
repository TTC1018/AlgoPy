import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = int(1e9)

def dfs(node):
    dp[node] = [0, 1] # node가 얼리어댑터인 경우/아닌 경우
    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)
            dp[node][0] += dp[nxt][1] # 내가 얼리어댑터 아니면 -> 다음 노드가 얼리어댑터
            dp[node][1] += min(dp[nxt]) # 내가 얼리어댑터면 -> 다음 노드가 뭐든 상관없고, 그중에 최소값 가져오기


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[INF] * 2 for _ in range(N + 1)]
visited = [False] * (N + 1)
visited[1] = True
dfs(1)
print(min(dp[1]))