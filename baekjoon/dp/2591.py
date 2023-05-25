import sys
input = sys.stdin.readline

N = input().rstrip()

dp = [0] * len(N)
c1 = set(range(1, 9 + 1))
c2 = set(range(10, 34 + 1))

if 1 <= int(N[0]) <= 9:
    dp[0] = 1
if 1 <= int(N[1]) <= 9:
    dp[1] = 1
if 10 <= int(N[:2]) <= 34:
    dp[1] += 1

for i in range(2, len(N)):
    if int(N[i]) in c1:
        dp[i] += dp[i - 1]
    if int(N[i - 1:i + 1]) in c2:
        dp[i] += dp[i - 2]
print(dp[len(N) - 1])
