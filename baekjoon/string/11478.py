import sys
input = sys.stdin.readline


S = input().rstrip()

substring = set()
for l in range(1, len(S) + 1):
    for i in range(len(S) + 1 - l):
        substring.add(S[i:i+l])
print(len(substring))