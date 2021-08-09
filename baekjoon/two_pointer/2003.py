N, M = tuple(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))

answer = 0
left = 0
right = 1
temp_sum = 0

while left <= right <= N:
    temp_sum = sum(A[left:right])
    if temp_sum == M:
        answer += 1

    if temp_sum >= M:
        left += 1
    elif temp_sum < M:
        right += 1


print(answer)