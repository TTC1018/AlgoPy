import sys
input = sys.stdin.readline


N = int(input())
IN = [input().rstrip() for _ in range(N)]
OUT = [input().rstrip() for _ in range(N)]

order = {IN[i]: i for i in range(N)}
answer = 0
for i in range(N):
    for j in range(i + 1, N):
        if order[OUT[i]] > order[OUT[j]]:
            answer += 1
            break
print(answer)
