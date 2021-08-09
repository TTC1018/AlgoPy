N, S = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

answer = N + 1
left, right = 0, 0
temp_sum = 0
while True:
    if temp_sum >= S:
        answer = min(answer, right - left)
        temp_sum -= nums[left]
        left += 1
    elif right == N:
        break
    else:
        temp_sum += nums[right]
        right += 1

if answer == N + 1:
    print(0)
else:
    print(answer)