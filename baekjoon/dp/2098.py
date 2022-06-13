import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
INF = int(1e9)


def tsp(now, mask):
    if mask == bit:
        return W[now][0] if W[now][0] else INF

    if dp[now][mask] == INF:
        min_val = INF
        for idx in range(N):
            if not (mask & (1 << idx)) and W[now][idx] != 0:
                min_val = min(min_val, tsp(idx, mask | (1 << idx)) + W[now][idx])
        dp[now][mask] = min_val if min_val != INF else INF - 1
    return dp[now][mask]


N = int(input())
bit = (1 << N) - 1
W = [list(map(int, input().split())) for _ in range(N)]
dp = [[INF] * (1 << N) for _ in range(N)]
print(tsp(0, 1))