import sys
input = sys.stdin.readline
in_range = lambda c: 0 <= c < 3
d = [-1, 0, 1]


order = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    dp = [[int(1e9)] * 3 for _ in range(N)]
    dp[0][1] = graph[0][1]
    dp[0][2] = graph[0][2] + dp[0][1]

    for row in range(1, N):
        for col in range(3):
            if in_range(col - 1):
                dp[row][col] = min(dp[row][col], graph[row][col] + dp[row][col - 1])

            for dc in d:
                nc = col + dc
                if in_range(nc):
                    dp[row][col] = min(dp[row][col], graph[row][col] + dp[row - 1][nc])

    print(f'{order}. {dp[N - 1][1]}')
    order += 1
