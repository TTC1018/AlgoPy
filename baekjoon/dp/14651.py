import sys
input = sys.stdin.readline


N = int(input())
dp = [[0] * 3 for _ in range(N + 1)]
dp[1][1] = 1; dp[1][2] = 1
for i in range(2, N + 1):
    for j in range(3):
        dp[i][j] += (sum(dp[i - 1]) % 1000000009)
print(dp[N][0])

# N자리 나머지 0
# => N-1자리 나머지 0에 0 잇기
# => N-1자리 나머지 1에 2 잇기
# => N-1자리 나머지 2에 1 잇기
# N자리 나머지 1
# => N-1자리 나머지 0에 1 잇기
# => N-1자리 나머지 1에 0 잇기
# => N-1자리 나머지 2에 2 잇기
...