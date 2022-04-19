dp = [0, 1, 1] + [-1] * (38)
for i in range(3, 40 + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

for _ in range(int(input())):
    N = int(input())
    if N == 0:
        print('1 0')
    else:
        print('{} {}'.format(dp[N - 1], dp[N]))