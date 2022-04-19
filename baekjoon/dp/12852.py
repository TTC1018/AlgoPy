N = int(input())

dp = [0, 0, 1, 1] + [0] * (N - 3)
for i in range(4, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
print(dp[N])
while N != 1:
    print(N, end=' ')
    cand = [(dp[N - 1], N - 1)]
    if N % 2 == 0:
        cand.append((dp[N // 2], N // 2))
    if N % 3 == 0:
        cand.append((dp[N // 3], N // 3))
    cand.sort()
    N = cand[0][1]
print(1)