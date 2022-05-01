from copy import deepcopy
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[0] + list(map(int, input().split())) for _ in range(N)]
graph.insert(0, [0] * (N + 1))
p_sum = deepcopy(graph)
# 첫줄 초기화
for i in range(1, N + 1):
    p_sum[1][i] += p_sum[1][i - 1]
    p_sum[i][1] += p_sum[i - 1][1]
for i in range(2, N + 1):
    for j in range(2, N + 1):
        p_sum[i][j] = p_sum[i][j] + p_sum[i][j - 1] + \
                      p_sum[i - 1][j] - p_sum[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = p_sum[x2][y2] - p_sum[x1 - 1][y2] - p_sum[x2][y1 - 1] + \
        p_sum[x1 - 1][y1 - 1]
    print(answer)