def dynamic_dfs(num):
    if dp[num] == -1:
        prevMax = 0
        for child in childs[num]:
            prevMax = max(prevMax, dynamic_dfs(child))
        dp[num] = prevMax + D[num]
    return dp[num]


INF = int(1e9)
for _ in range(int(input())):
    N, K = map(int, input().split())
    D = [-1] + list(map(int, input().split()))
    
    childs = [[] for _ in range(N + 1)]
    for i in range(K):
        X, Y = map(int, input().split())
        childs[Y].append(X)
    W = int(input())
    
    dp = [-1] * (N + 1)
    for i in range(1, N + 1):
        dynamic_dfs(i)
    print(dp[W])