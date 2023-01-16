import sys


N, M, K = map(int, input().split())
dp = [[1] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # 이전 글자 앞에 a를 이은 경우 + z를 이은 경우

if K > dp[N][M]: # 최대 경우의 수보다 요청 수가 크다면
    print(-1)
    sys.exit()

answer = ''
while N > 0 and M > 0:
    split = dp[N - 1][M]
    if K <= split: # 다음 단어가 a
        N -= 1
        answer += 'a'
    else: # 다음 단어가 z
        M -= 1
        K -= split # 불가능한 후보군 제거
        answer += 'z'
else:
    answer += ('a' * N + 'z' * M) # 남은 알파벳 이어주기

print(answer)
