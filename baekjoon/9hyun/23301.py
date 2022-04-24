from collections import defaultdict
import sys
input = sys.stdin.readline


N, T = map(int, input().split())
study = defaultdict(int)
min_time, max_time = 1000, 0
for _ in range(N):
    K = int(input())
    for _ in range(K):
        S, E = map(int, input().split())
        min_time = min(min_time, S)
        max_time = max(max_time, E)
        for i in range(S, E):
            study[i] += 1

answer = []
ans_val = 0
for i in range(min_time, max_time - 1):
    temp_val = 0
    for j in range(i, i + T):
        temp_val += study[j]

    if ans_val < temp_val:
        answer = [(i, i + T)]
        ans_val = temp_val
    elif ans_val == temp_val:
        answer.append((i, i + T))
answer.sort()
print(*answer[0])