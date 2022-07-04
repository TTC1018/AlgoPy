import sys
input = sys.stdin.readline


def min_cost(x, y):
    if x == y:
        dp[x][y] = P[x]
        return dp[x][y]

    if dp[x][y] == INF:
        for k in range(x, y):
            # P[x] ~ P[y] 최소합 = P[x] ~ P[k] 최소합 + P[k + 1] ~ P[y] 최소합
            dp[x][y] = min(dp[x][y], min_cost(x, k) + min_cost(k + 1, y))
        dp[x][y] += (psum[y + 1] - psum[x])
    return dp[x][y]



INF = int(1e9)
for _ in range(int(input())):
    K = int(input())
    P = list(map(int, input().split()))

    psum = [0] + P[:] # psum[x][y] = P[x] ~ P[y] 합
    for i in range(K):
        psum[i + 1] += psum[i]

    dp = [[INF] * K for _ in range(K)] # dp[x][y] = P[x] ~ P[y] 최소합
    print(min_cost(0, K - 1) - psum[K]) # 합치기가 완성되면 누적합을 더하지 않기 때문에 다시 빼줌