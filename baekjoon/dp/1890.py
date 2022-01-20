N = int(input())
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        for prev in range(i):
            if m[prev][j] == i - prev:
                dp[i][j] += dp[prev][j]
        for prev in range(j):
            if m[i][prev] == j - prev:
                dp[i][j] += dp[i][prev]
print(dp[N - 1][N - 1])