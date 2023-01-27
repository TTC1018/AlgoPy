import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = list(map(int, input().split()))

# 최솟값을 이분탐색
start, end = max(L), int(1e9)
while start <= end:
    mid = (start + end) // 2

    # 가능한지 확인
    tmp, cnt = 0, 0
    for i in range(N - 1, -1, -1):
        tmp += L[i]
        if tmp > mid:
            tmp = L[i]
            cnt += 1
        elif tmp == mid:
            tmp = 0
            cnt += 1
    else:
        if tmp != 0:
            cnt += 1
        if cnt <= M:
            end = mid - 1
            continue
    start = mid + 1

print(end + 1)