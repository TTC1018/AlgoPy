N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]
LIMIT = N * 10000

K = 0
start, end = max(money), LIMIT
while start <= end:
    mid = (start + end) // 2
    
    cnt, rest = 1, mid
    for m in money:
        if m > rest:
            cnt += 1
            rest = mid - m
        else:
            rest -= m
    
    if cnt <= M:
        end = mid - 1
        K = mid
    else:
        start = mid + 1
print(K)