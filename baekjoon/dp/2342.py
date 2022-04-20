INF = int(1e9)
ops = list(map(int, input().split()))
feet = [0, 0]

dp = [INF for _ in range(len(ops) + 1)]
dp[1], feet[0] = 2, ops[0]
dp[2], feet[1] = 4, ops[1]

for i in range(2, len(ops)):
    if ops[i] in feet:
        dp[i] = min(dp[i], dp[i - 1] + 1)
    else:
        
