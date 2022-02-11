N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

start, end = 1, houses[-1] - houses[0] # 가능한 최소갭 & 최대갭
answer = 0
while start <= end:
    mid = (start + end) // 2
    point = houses[0] # 첫 집부터 확인
    set_count = 1

    for i in range(1, N):
        if houses[i] >= point + mid: # 현재 집에서 gap 만큼 간 거리보다 다음 집이 멀 때 (목표거리 충족)
            point = houses[i]
            set_count += 1

    if set_count >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)