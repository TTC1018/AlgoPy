import sys
input = sys.stdin.readline


N = int(input())
L = [tuple(map(int, input().split())) for _ in range(N)]
L.sort()

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if L[j][0] < L[i][0] and L[j][1] < L[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))