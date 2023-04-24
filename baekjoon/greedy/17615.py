import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

lr_cnt, rr_cnt = 0, 0
l_idx, r_idx = 0, N - 1
while r_idx >= 0 and S[r_idx] == 'R':
    rr_cnt += 1
    r_idx -= 1
while l_idx < N and S[l_idx] == 'R':
    lr_cnt += 1
    l_idx += 1

bl_cnt, br_cnt = 0, 0
l_idx, r_idx = 0, N - 1
while r_idx >=0 and S[r_idx] == 'B':
    br_cnt += 1
    r_idx -= 1
while l_idx < N and S[l_idx] == 'B':
    bl_cnt += 1
    l_idx += 1

b_cnt, r_cnt = S.count('B'), S.count('R')
print(min(min(b_cnt - bl_cnt, b_cnt - br_cnt), min(r_cnt - lr_cnt, r_cnt - rr_cnt)))
