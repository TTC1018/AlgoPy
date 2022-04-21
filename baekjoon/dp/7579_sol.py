import sys
input = sys.stdin.readline


INF = int(1e9)
N, M = map(int, input().split()) # 앱 개수, 필요한 메모리
m = list(map(int, input().split())) # 활성화 상태에서 차지하는 메모리
c = list(map(int, input().split())) # 비활성화 -> 활성화 하는 비용
c_limit = sum(c)
dp = [[0] * (c_limit + 1) for _ in range(N + 1)] # 행: 어플 N개 끄기까지 / 열: 소모된 비용 cost

for i in range(1, N + 1):
    for j in range(c_limit + 1):
        dp[i][j] = max(dp[i][j], dp[i - 1][j]) # 어플 한개 덜 끄기 전 비용으로 초기화
        
        diff = j - c[i - 1] # 감당 가능한 cost 일때
        if diff >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][diff] + m[i - 1])

for i in range(c_limit + 1):
    if dp[N][i] >= M:
        print(i)
        break