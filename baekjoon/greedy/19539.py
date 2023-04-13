import sys
input = sys.stdin.readline


N = int(input())
h = list(map(int, input().split()))

total = sum(h)
if total % 3 != 0:
    print('NO')
else:
    if sum(num // 2 for num in h) >= total // 3:
        print('YES')
    else:
        print('NO')
