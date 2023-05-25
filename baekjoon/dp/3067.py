import sys
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    C = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1
    for c in C:
        for price in range(1, M + 1):
            if c <= price:
                dp[price] += dp[price - c]
    print(dp[M])