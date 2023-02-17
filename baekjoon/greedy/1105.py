import sys
input = sys.stdin.readline

L, R = map(int, input().split())
max_val = len(str(L))

l_len = len(str(L))
r_len = len(str(R))

if l_len < r_len:
    print(0)
elif l_len == r_len:
    if L == R:
        print(str(L).count('8'))
    else:
        tmp = 0
        for i in range(l_len):
            if str(L)[i] != str(R)[i]:
                break
            if str(L)[i] == '8':
                tmp += 1
        print(tmp)
