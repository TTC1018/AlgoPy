import sys
input = sys.stdin.readline


def check(num_val):
    grouped = 1

    sum_val = 0
    for b in biz:
        sum_val += b
        if sum_val > num_val:
            grouped += 1
            sum_val = b

    return grouped <= M


N, M = map(int, input().split())
biz = list(map(int, input().split()))
start, end = max(biz), sum(biz)
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        end = mid - 1
    else:
        start = mid + 1

b_cnt = 0
total = 0
answer = []
limit = M
for i in range(N):
    total += biz[i]
    if total > start:
        answer.append(b_cnt)
        total = biz[i]
        b_cnt = 0
        limit -= 1
    b_cnt += 1
    if N - i == limit:
        answer.append(b_cnt)
        limit -= 1
        break
answer.extend([1 for _ in range(limit)])


print(start)
print(*answer)