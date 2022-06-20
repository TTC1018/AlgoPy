import sys
input = sys.stdin.readline

N, C = map(int, input().split())
H = [int(input()) for _ in range(N)]
H.sort()

answer = 0
start, end = 1, H[-1]
while start <= end:
    mid = (start + end) // 2

    cnt, point = 1, H[0]
    for h in H:
        if point + mid <= h: # 설정 거리 이내
            cnt += 1
            point = h

    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1
print(start - 1)
