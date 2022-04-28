import sys
input = sys.stdin.readline


N = int(input())
visited = 1 << 10 # 2^10 = 1024
# 9 8 7 6 5 4 3 2 1 0 -> 10개
# X X X X X X X X X X -> 사용했을 때 1로 표현
# 예) 4 3 2 를 사용한 경우 0 0 0 0 0 1 1 1 0 0 = 28
# 최대는 1 1 1 1 1 1 1 1 1 1 (1023)

dp = [[[0] * visited for _ in range(9 + 1)] for _ in range(N + 1)]
# 길이가 N이면서, X로 끝나고, 0 ~ 9 사이의 특정 숫자를 사용한 계단수를 기록

for i in range(1, 9 + 1):
    dp[1][i][1 << i] = 1 # 한자리 계단수

for i in range(2, N + 1):
    for j in range(9 + 1):
        for k in range(visited): # 0 ~ 1023
            bit_mask = k | (1 << j) # 숫자 j 사용 포함
            dp[i][j][bit_mask] = (dp[i][j][bit_mask] + 
                                  ((dp[i - 1][j - 1][k] if j != 0 else 0) +
                                  (dp[i - 1][j + 1][k] if j != 9 else 0)) % 10**9
                                    ) % 10**9

answer = 0
for i in range(9 + 1):
    answer = (answer + dp[N][i][-1]) % 10**9 # 0 ~ 9 다 쓴 계단수만 합산
print(answer)