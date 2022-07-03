import sys
input = sys.stdin.readline


S = input().rstrip()
S = S.split('-')

s_len = len(S)
answer = sum([int(s) for s in S[0].split('+')])
for i in range(1, s_len):
    answer -= sum([int(s) for s in S[i].split('+')])
print(answer)