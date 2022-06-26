import sys
input = sys.stdin.readline


S = input().rstrip()
answer = S[0]

for i in range(1, len(S)):
    if answer[0] < S[i]:
        answer += S[i]
    else:
        answer = S[i] + answer
print(answer)