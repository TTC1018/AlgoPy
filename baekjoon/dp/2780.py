import sys
input = sys.stdin.readline

P = {
    1: [2, 4], 2: [1, 3, 5], 3: [2, 6],
    4: [1, 5, 7], 5: [2, 4, 6, 8], 6: [3, 5, 9],
    7: [0, 4, 8], 8: [5, 7, 9], 9: [6, 8],
    0: [7]
}
dp = [[0] * (9 + 1) for _ in range(1000 + 1)]
for num in range(9 + 1):
    dp[1][num] = 1
for l in range(2, 1000 + 1):
    for num in range(9 + 1):
        for prev in P[num]:
            dp[l][num] += dp[l - 1][prev]
        dp[l][num] %= 1234567

for _ in range(int(input())):
    print(sum(dp[int(input())]) % 1234567)