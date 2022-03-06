n = int(input())
dp = [0] * (n + 1)
dp[1] = 1

idx = [1, 1, 1]
next = [2, 3, 5]
for i in range(2, n + 1):
    dp[i] = min(next)

    if dp[i] == next[0]:
        idx[0] += 1
        next[0] = dp[idx[0]] * 2
    if dp[i] == next[1]:
        idx[1] += 1
        next[1] = dp[idx[1]] * 3
    if dp[i] == next[2]:
        idx[2] += 1
        next[2] = dp[idx[2]] * 5

print(dp[n])