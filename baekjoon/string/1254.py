import sys
input = sys.stdin.readline


S = input().rstrip()

for i in range(len(S) + 1):
    new_S = S + S[:i][::-1]
    if new_S == new_S[::-1]:
        print(len(new_S))
        break