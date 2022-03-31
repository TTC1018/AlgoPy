N = int(input())
rcs = []
for _ in range(N):
    r, c = map(int, input().split())
    rcs.append((r, c))

answer = 0
if N == 1:
    answer = 0
elif N == 2:
    answer += (rcs[0][0] * rcs[0][1] * rcs[1][1])
else:
    dp = [0] * N
    for i in range(1, N):
        dp[i] = min()