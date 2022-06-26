from bisect import bisect_left
import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))

seq = [0]
idx_list = [0] * N
max_idx = 1

for i in range(N):
    if A[i] > seq[-1]:
        seq.append(A[i])
        idx_list[i] = max_idx
        max_idx += 1
    else:
        new_idx = bisect_left(seq, A[i])
        seq[new_idx] = A[i]
        idx_list[i] = new_idx

max_idx -= 1
answer = []
for i in range(N - 1, -1, -1):
    if idx_list[i] == max_idx:
        answer.append(A[i])
        max_idx -= 1

answer.reverse()
print(len(answer))
print(*answer)