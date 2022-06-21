from collections import deque
import sys
input = sys.stdin.readline

# BABA
# BAB + A
# ABA + B & 뒤집기
S = list(input().rstrip())
T = list(input().rstrip())

s_len, t_len = len(S), len(T)
r_flag = False

cnt = t_len
for i in range(t_len - 1, -1, -1):
    if T[i] == 'A':
        T.pop()
    elif T[i] == 'B':
        if r_flag:
            T.pop()
        else:
            T.pop(0)
        r_flag = not r_flag

    cnt -= 1
    if cnt == s_len:
        if r_flag:
            T = T[::-1]
        break

if S == T:
    print(1)
else:
    print(0)