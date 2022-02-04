from copy import deepcopy

n = int(input())
tri = []
dp = [[] for _ in range(n)]
for i in range(n):
    tri.append(list(map(int, input().split())))
    dp[i] = deepcopy(tri[i])

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + tri[i][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] = dp[i - 1][-1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i][j]

print(max(dp[-1]))