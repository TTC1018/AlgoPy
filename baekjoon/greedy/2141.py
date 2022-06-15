import sys
input = sys.stdin.readline

N = int(input())
XA = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
XA.sort(key=lambda x: x[0])
half = sum([xa[1] for xa in XA]) / 2

cnt = 0
for X, A in XA:
    cnt += A
    if cnt >= half:
        print(X)
        sys.exit()
print(0)
