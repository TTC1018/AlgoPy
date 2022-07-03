import sys
input = sys.stdin.readline


S = input().rstrip()
s_len = len(S)
S = '\n'.join(sorted([S[-i:] for i in range(1, s_len + 1)]))
print(S)