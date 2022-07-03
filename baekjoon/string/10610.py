import sys
input = sys.stdin.readline


N = list(input().rstrip())
if not sum(map(int, N)) % 3 and '0' in N:
    N = ''.join(sorted(N, reverse=True))
    print(N)
else:
    print(-1)