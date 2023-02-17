import sys
input = sys.stdin.readline

L, R = input().rstrip().split()
l_len = len(L)
r_len = len(R)

if l_len < r_len:
    print(0)
elif l_len == r_len:
    if L == R:
        print(L.count('8'))
    else:
        tmp = 0
        for i in range(l_len):
            if L[i] != R[i]:
                break
            if L[i] == '8':
                tmp += 1
        print(tmp)
