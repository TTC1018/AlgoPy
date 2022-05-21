import sys
input = sys.stdin.readline


N, K = map(int, input().split())
W = [-1]
V = [-1]
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
dp = [[0] * (K + 1) for _ in range(N + 1)] # N번째 물건까지 썼을 때, K 이하의 무게로 채운 가치값
for i in range(1, N + 1):
    for weight in range(1, K + 1):
        dp[i][weight] = dp[i - 1][weight] # 초기화
        if weight >= W[i]: # 담을 수 있는 물건이면
            dp[i][weight] = max(dp[i][weight], dp[i - 1][weight - W[i]] + V[i])
print(dp[N][K])