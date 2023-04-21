import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
B = input().rstrip()
dp = [INF] * N
P = {'B': 'J', 'O': 'B', 'J': 'O'}

dp[0] = 0
for now in range(1, N):
    for prev in range(now):
        if P[B[now]] == B[prev]:
            dp[now] = min(dp[now], dp[prev] + (now - prev)**2)
print(dp[N - 1] if dp[N - 1] != INF else -1)
