N, M = map(int, input().split())

dp = [-1] * 10001
d = dict()
for i in range(N):
    d[int(input())] = True

for k in d:
    dp[k] = 1

for i in range(1, M + 1):
    for k in d:
        if dp[i - k] != -1:
            dp[i] = dp[i - k] + 1 if dp[i] == -1 else min(dp[i], dp[i - k] + 1)

print(dp)
print(dp[M])