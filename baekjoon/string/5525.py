import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
S = input().rstrip()

answer = 0
idx = 0
ioi_cnt = 0
while idx < M:
    if S[idx:idx+3] == 'IOI':
        idx += 2
        ioi_cnt += 1

        if ioi_cnt == N:
            answer += 1
            ioi_cnt -= 1
    else:
        idx += 1
        ioi_cnt = 0
print(answer)