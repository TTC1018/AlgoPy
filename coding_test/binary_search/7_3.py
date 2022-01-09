N, M = map(int, input().split())
dduck = list(map(int, input().split()))

start, end = 0, max(dduck)
answer = 0
while start <= end:
    t_sum = 0
    mid = (start + end) // 2
    for dd in dduck:
        if dd > mid:
            t_sum += dd - mid

    if t_sum >= M:
        answer = mid
        start = mid + 1
    elif t_sum < M:
        end = mid - 1

print(answer)