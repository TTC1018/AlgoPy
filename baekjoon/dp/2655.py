import sys
input = sys.stdin.readline


N = int(input())
brick = [tuple(map(int, input().split())) for _ in range(N)]
idx_dict = dict()
for i in range(N):
    idx_dict[(brick[i][0], brick[i][2])] = i + 1

brick.sort(key=lambda x:-x[0]) # 넓이 순 내림차순 정렬
dp = [[brick[i][1], str(idx_dict[(brick[i][0], brick[i][2])])] for i in range(N)]
for i in range(1, N):
    for j in range(i):
        if brick[j][2] > brick[i][2]: # 무게 더 무거운 경우
            if dp[i][0] < dp[j][0] + brick[i][1]:
                dp[i] = [dp[j][0] + brick[i][1], dp[j][1] + '/' + str(idx_dict[(brick[i][0], brick[i][2])])]
dp.sort()
answer = list(dp[-1][1].split('/'))[::-1]
print(len(answer))
for idx in answer:
    print(idx)