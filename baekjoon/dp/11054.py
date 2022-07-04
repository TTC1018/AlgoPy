import sys
input = sys.stdin.readline


N = int(input())
S = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for idx in range(1, N):
    for left in range(idx):
        if S[left] < S[idx]:
            dp[idx] = max(dp[idx], dp[left] + 1)

for idx in range(1, N):
    for left in range(idx):
        if S[left] > S[idx]:
            dp[idx] = max(dp[idx], dp[left] + 1)

print(max(dp))
