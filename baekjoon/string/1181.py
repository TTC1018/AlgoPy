import sys
input = sys.stdin.readline


N = int(input())
S = [input().rstrip() for _ in range(N)]
S = list(set(S))
S.sort(key=lambda x:(len(x), x))

for s in S:
    print(s)