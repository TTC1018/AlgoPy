from copy import deepcopy

T = int(input())
direction = [(-1, -1), (0, -1), (1, -1)] # 왼쪽 위 / 왼쪽 / 왼쪽 아래

for i in range(T):
    n, m = map(int, input().split())
    golds = list(map(int, input().split()))
    dp = deepcopy(golds)

    for j in range(1, m):
        for i in range(n):
            for d in direction: # 현재 위치로 올 수 있는 경로들
                nx, ny = i + d[0], j + d[1]
                if 0 <= nx < n and 0 <= ny < m: # 가능한 이전 위치인지 확인
                    dp[i * m + j] = max(dp[i * m + j], golds[i * m + j] + dp[nx * m + ny]) # 가능한 경로들 중에 최대값을 선택

    answer = 0
    for i in range(n):
        answer = max(answer, dp[i * m + m - 1]) # 열 끝에 있는 칸이 최종 지점들의 후보이므로 하나씩 확인
    print(answer)


