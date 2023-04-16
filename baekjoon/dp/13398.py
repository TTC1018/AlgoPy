import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(n)]
dp[0][0] = num[0]

answer = num[0]
for i in range(1, n):
    dp[i][0] = max(num[i], dp[i - 1][0] + num[i]) # 연속 끊기 vs. 이어나가기
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + num[i]) # 나 제외하고 이어나가기 vs. 나 포함 이어나가기
    answer = max(answer, max(dp[i]))
print(answer)