import sys
input = sys.stdin.readline


N, M = map(int, input().split())
d = {input().rstrip():True for _ in range(N)}

answer = 0
for _ in range(M):
    if input().rstrip() in d:
        answer += 1
print(answer)