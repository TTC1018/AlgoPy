import sys
input = sys.stdin.readline


N, M = map(int, input().split())
R = list(map(int, input().split()))
if N <= M:
    print(N)
    sys.exit()


start, end = 1, N * max(R) # 마지막 아이가 탑승했을 때의 시간 찾기
time = 0
while start <= end:
    mid = (start + end) // 2
    cnt = M

    for r in R:
        cnt += (mid // r) # 시간 내에 놀이기구가 태울 수 있는 인원의 수

    if cnt >= N:
        time = mid
        end = mid - 1
    else:
        start = mid + 1

child = M + sum([(time - 1) // r for r in R]) # time 되기 1초 전까지 태운 인원
for i in range(M):
    if not time % R[i]: # time에 내릴 때
        child += 1

    if child == N:
        print(i + 1)
        break