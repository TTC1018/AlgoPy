import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
INF = int(1e9)


def calc_dist(a, b, c, d):
    return ((a - c)**2 + (b - d)**2) ** 0.5


def tsp(now, mask):
    if mask == whole_bit:
        nx, ny = pos[now]
        return calc_dist(pos[0][0], pos[0][1], nx, ny)

    if dp[now][mask] == INF:
        x, y = pos[now]
        min_val = INF
        for nxt in range(N):
            be_covered = 1 << nxt
            if not (mask & be_covered):
                nx, ny = pos[nxt]
                min_val = min(min_val, tsp(nxt, mask | be_covered) + calc_dist(x, y, nx, ny))
        dp[now][mask] = min_val if min_val != INF else INF - 1
    return dp[now][mask]


N = int(input())
pos = [(tuple(map(int, input().split()))) for _ in range(N)]
dp = [[INF] * (1 << N) for _ in range(N)]
whole_bit = (1 << N) - 1
print(tsp(0, 1))