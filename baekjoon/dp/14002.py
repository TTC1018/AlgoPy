import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
dp = [1] * N
for idx in range(N):
    for j in range(idx):
        if A[idx] > A[j]:
            dp[idx] = max(dp[idx], dp[j] + 1)

max_cnt = max(dp)
max_idx = dp.index(max_cnt)
answer = [A[max_idx]]

cnt = 1
idx = max_idx - 1
while cnt < max_cnt:
    if A[idx] < A[max_idx] and dp[idx] == dp[max_idx] - 1:
        answer.append(A[idx])
        max_idx = idx
        cnt += 1
    idx -= 1

print(max_cnt)
print(*reversed(answer))