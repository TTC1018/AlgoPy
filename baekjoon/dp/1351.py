# 재귀 + DP
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def btk(now):
    if dp[now] != 0:
        return dp[now]

    dp[now] = btk(now // P) + btk(now // Q)
    return dp[now]


N, P, Q = map(int, input().split())
dp = defaultdict(int)
dp[0] = 1
print(btk(N))