from copy import deepcopy

T = int(input())
direction = [(-1, -1), (0, -1), (1, -1)] # 왼쪽 위 / 왼쪽 / 왼쪽 아래

for i in range(T):
    n, m = map(int, input().split())
    golds = list(map(int, input().split()))
    dp = deepcopy(golds)

    for j in range(1, m):
        for i in range(n):
            for d in direction:
                nx, ny = i + d[0], j + d[1]
                if 0 <= nx < n and 0 <= ny < m:
                    dp[i * m + j] = max(dp[i * m + j], golds[i * m + j] + dp[nx * m + ny])

    answer = 0
    for i in range(n):
        answer = max(answer, dp[i * m + m - 1])
    print(answer)


