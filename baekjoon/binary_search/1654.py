K, N = map(int, input().split())

lans = []
for i in range(K):
    lans.append(int(input()))

start, end = 1, max(lans)

answer = 0
while start <= end:
    mid = (start + end) // 2

    t_count = 0
    for l in lans:
        t_count += (l // mid)

    if t_count < N:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)
