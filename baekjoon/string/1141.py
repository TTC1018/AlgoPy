import sys
input = sys.stdin.readline


N = int(input())
S = sorted(input().rstrip() for _ in range(N))

answer = 1
for i in range(1, N):
    if len(S[i - 1]) <= len(S[i]):
        if S[i - 1] != S[i][:len(S[i - 1])]:
            answer += 1
    else:
        if S[i] != S[i - 1][:len(S[i])]:
            answer += 1
print(answer)