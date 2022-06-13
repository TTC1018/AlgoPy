import sys
input = sys.stdin.readline

P = input().rstrip()
S = input().rstrip()

if S in P:
    print(1)
else:
    print(0)
