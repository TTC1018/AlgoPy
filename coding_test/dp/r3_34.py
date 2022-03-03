N = int(input())
soldiers = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i): # 인덱스 0 부터 내림차순으로 이어질 수 있는지 확인
        if soldiers[i] < soldiers[j]: # 내림차순 충족할 때
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
