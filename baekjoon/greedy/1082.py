N = int(input())
P = list(map(int, input().split()))
M = int(input())

dp = [-5001] * (M + 1)
for i in range(N - 1, -1, -1): # 번호 역순으로
    target = P[i]
    for j in range(target, M + 1):
        dp[j] = max(dp[j], dp[j-target]*10 + i, i) # P[i]만큼 쓰기 전에 구성된 숫자에 i 갖다 붙이기 vs P[i] 만큼만 사용하기
print(dp[M])