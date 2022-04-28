import sys
input = sys.stdin.readline


S = 1
# 특정 수를 갖고 있을 때 해당 위치 비트를 1로 바꿔주기
# 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 공
# 0  0  0  0  0  0  0  0  0  0  0  0 0 0 0 0 0 0 0 0 1
for _ in range(int(input())):
    ipt = input().split()
    op = ipt[0]
    
    if op == 'add':
        x = int(ipt[1])
        S = S | (1 << x)
    elif op == 'remove':
        x = int(ipt[1])
        S = S & ((1 << 21) - 1 - (1 << x))
    elif op == 'check':
        x = int(ipt[1])
        if S & (1 << x):
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        x = int(ipt[1])
        if S & (1 << x):
            S = S & ((1 << 21) - 1 - (1 << x))
        else:
            S = S | (1 << x)
    elif op == 'all':
        S = (1 << 21) - 1 # 비트 전부 1로 바꾸기
    elif op == 'empty':
        S = 1