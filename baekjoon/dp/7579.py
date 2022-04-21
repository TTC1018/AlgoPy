# 메모리 초과

import sys
input = sys.stdin.readline


INF = int(1e9)
N, M = map(int, input().split()) # 앱 개수, 필요한 메모리
m = list(map(int, input().split())) # 활성화 상태에서 차지하는 메모리
c = list(map(int, input().split())) # 비활성화 -> 활성화 하는 비용

# 최소 비용으로 메모리 확보하기
dp = [(INF, []) for _ in range(sum(m) + 1)]
dp[0] = [0, []]
for i in range(N):
    dp[m[i]] = [c[i], [m[i]]]
for i in range(1, M + 1):
    target = i # 30
    for j in range(N):
        diff = target - m[j] # 0, 20, 10
        if diff >= 0:
            if m[j] not in dp[diff][1]:
                if dp[diff][0] + c[j] < dp[i][0]:
                    dp[i] = (dp[diff][0] + c[j], dp[diff][1] + [m[j]])

answer = INF
for i in range(M, sum(m) + 1):
    answer = min(answer, dp[M][0])
print(answer)