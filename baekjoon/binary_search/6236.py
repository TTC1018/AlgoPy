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
        if mid_copy < s: # 남은 돈 < 뽑을 돈 이면
            mid_copy = mid # 남은 돈을 다시 뽑은 돈으로 초기화
            count += 1 # 돈 뽑은 횟수 추가

        mid_copy -= s # 남은 돈 - 뽑을 돈

    if count > M:
        start = mid + 1
    else: # 뽑은 횟수 = 뽑아야 되는 횟수, 뽑은 횟수 < 뽑아야 되는 횟수
        end = mid - 1
        answer = mid
print(answer)