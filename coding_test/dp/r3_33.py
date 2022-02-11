N = int(input())
works = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * N
if works[0][0] == 1:
    dp[0] = works[0][1]

for i in range(1, N):
    if works[i][0] == 1: # 당일의 일을 그 날에 처리 가능하면 그 값으로 초기화
        dp[i] = works[i][1] + dp[i - 1]
    else: # 처리 불가능하면 이전 값으로 초기화 (현재까지 최대값)
        dp[i] = dp[i - 1]

    for j in range(i):
        if works[j][0] - 1 + j == i: # j일부터 N일 걸려서 i일에 마감 가능한 일인 경우
            if j != 0:
                dp[i] = max(dp[i], dp[j - 1] + works[j][1])
            else: # j == 0 일때의 경우를 필터링해줘야함 (아니면 dp[j - 1]에 dp[-1]이 들어가버림)
                dp[i] = max(dp[i], works[j][1])

print(dp[N - 1])