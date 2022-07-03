import sys
input = sys.stdin.readline


N = list(input().rstrip())
print(''.join(sorted(N, reverse=True)))