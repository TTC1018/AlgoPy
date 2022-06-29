import sys
input = sys.stdin.readline


def dfs(now, mask, price):
    if dp[now][mask][price] == -1:
        dp[now][mask][price] = 1
        max_val = 0
        for nxt in range(N):
            if P[now][nxt] >= price and not (mask & (1 << nxt)):
                max_val = max(max_val, dfs(nxt, mask | (1 << nxt), P[now][nxt]))
        dp[now][mask][price] += max_val
    return dp[now][mask][price]


N = int(input())
P = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dp = [[[-1] * 10 for _ in range(1 << 16)] for _ in range(N)]
print(dfs(0, 1 << 0, 0))
