import sys
input = sys.stdin.readline


INF = int(1e9)
N = int(input())
dp = [[0, 0, 0] for _ in range(N + 1)]
paint = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

answer = INF
for i in range(3):
    dp[1][i] = paint[1][i] # 첫번째로 쓸 색을 설정
    for j in [n for n in range(3) if n != i]:
        dp[1][j] = INF # 나머지는 선택 안 될 값으로 설정

    for j in range(2, N + 1):
        red, green, blue = paint[j]
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + red
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + green
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + blue

    answer = min(answer, min([a for idx, a in enumerate(dp[N]) if idx != i])) # 처음 쓴 색과 다른 것중에 최소 선택
print(answer)