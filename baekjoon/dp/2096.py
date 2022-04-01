from copy import deepcopy
INF = int(1e9)

N = int(input())
dp = [[0, INF] for _ in range(3)]
# 초기화
row = list(map(int, input().split()))
for i in range(3):
    dp[i] = [row[i], row[i]]

# DP
for i in range(N - 1):
    row = list(map(int, input().split()))
    temp_dp = deepcopy(dp)
    for j in range(3):
        dp[j][0] = row[j] + max([temp_dp[pj][0] for pj in range(j - 1, j + 2) if 0 <= pj < 3])
        dp[j][1] = row[j] + min([temp_dp[pj][1] for pj in range(j - 1, j + 2) if 0 <= pj < 3])

# 답 구하기
dp_max, dp_min = 0, INF
for i in range(3):
    dp_max, dp_min = max(dp_max, dp[i][0]), min(dp_min, dp[i][1])
print(dp_max, dp_min)