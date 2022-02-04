N, M = map(int, input().split())

spending = []
for _ in range(N):
    spending.append(int(input()))

start, end = max(spending), 10000 * N
answer = 0
while start <= end:
    mid = (start + end) // 2

    count, mid_copy = 1, mid
    for s in spending:
        if mid_copy < s:
            mid_copy = mid
            count += 1

        mid_copy -= s

    if count > M:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid
print(answer)