import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
C = [tuple(map(int, input().split())) for _ in range(k)]
dp = [0] * (T + 1)
dp[0] = 1

for p, n in C:
    for t in range(T, 0 - 1, -1):
        if dp[t]: # 0이상 이어야 더할 가치가 있음
            for cnt in range(1, n + 1):
                cost = t + p * cnt # t원에 동전 cnt개를 더해서 만들 수 있는 금액
                if cost > T:
                    break

                dp[cost] += dp[t]
print(dp[T])
