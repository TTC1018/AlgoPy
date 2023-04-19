import sys
input = sys.stdin.readline


N, T = map(int, input().split())
C = sorted(tuple(map(int, input().split())) for _ in range(N))
dp = [0] * (T + 1)
for K, S in C:
    for t in range(T, -1, -1): # 역으로 내려오면서 중복 계산 방지
        if K > t:
            break

        dp[t] = max(dp[t], dp[t - K] + S)
print(dp[T])