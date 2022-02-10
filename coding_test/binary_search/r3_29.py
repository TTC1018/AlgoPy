N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

start, end = 1, houses[-1] - houses[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    point = houses[0]
    set_count = 1
    for i in range(1, N):
        if houses[i] >= point + mid:
            point = houses[i]
            set_count += 1

    if set_count >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)