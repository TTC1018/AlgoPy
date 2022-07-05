import sys
input = sys.stdin.readline


A, B = input().rstrip().split()
a_len, b_len = len(A), len(B)

max_cnt = 0
for i in range(b_len - a_len + 1):
    cnt = 0
    for j in range(a_len):
        if A[j] == B[i+j]:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
print(a_len - max_cnt)