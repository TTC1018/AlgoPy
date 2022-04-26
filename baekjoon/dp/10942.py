import sys
input = sys.stdin.readline


N = int(input())
NUM = list(map(int, input().split()))
dp = [[False] * N for _ in range(N)] # dp[s][e] = s인덱스부터 e인덱스까지의 문자열이 팰린드롬인지를 기록
# 1개 짜리 팰린드롬 초기화
for i in range(N):
    dp[i][i] = True
# 2개 짜리 팰린드롬 초기화
for i in range(N - 1):
    if NUM[i] == NUM[i + 1]:
        dp[i][i + 1] = True
# 3개 이상
# 특정 문자열이 팰린드롬 인지는
# 첫번째와 끝 문자열이 같고 그 사이의 문자열이 팰린드롬인지만 확인하면 됨
# NUM[0] NUM[3] dp[1][2]
# NUM[1] NUM[4] dp[2][3]
# ...
# NUM[3] NUM[6] dp[4][5]
for i in range(2, N): # 길이
    for j in range(N - i):
        if NUM[j] == NUM[j + i] and dp[j + 1][j + i - 1]:
            dp[j][j + i] = True

for _ in range(int(input())):
    S, E = map(int, input().split())
    if dp[S - 1][E - 1]:
        print(1)
    else:
        print(0)