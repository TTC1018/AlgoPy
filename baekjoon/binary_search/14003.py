import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
sequence = [-10**9 - 1]
idx_list = [0] * N # A[i]가 LIS 리스트에서 어떤 인덱스를 차지했는지 기록
max_idx = 0 # LIS 리스트 길이 기록

for i in range(N):
    if sequence[-1] < A[i]:
        sequence.append(A[i])
        idx_list[i] = len(sequence) - 1
        max_idx = idx_list[i]
    else:
        idx_list[i] = bisect_left(sequence, A[i])
        sequence[idx_list[i]] = A[i]
sequence.pop(0)

print(idx_list)
answer = []
for i in range(N - 1, -1, -1): # 가장 마지막으로 자리를 대체한 값을 우선으로 찾기 위해 역으로 탐색
    if idx_list[i] == max_idx:
        answer.append(A[i])
        max_idx -= 1

answer.reverse()
print(len(answer))
print(*answer)