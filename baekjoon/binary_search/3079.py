import sys
input = sys.stdin.readline


N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]

answer = 0
start, end = 1, max(T) * M
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for t in T:
        cnt += (mid // t)

    if cnt >= M:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
print(answer)