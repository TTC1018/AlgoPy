N, S = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

left, right = 0, 1
answer = 0

abs_S = abs(S)
while left <= right <= N:
    temp_sum = abs(sum(nums[left:right]))
    if temp_sum == abs_S:
        print(left, right)
        answer += 1

    if temp_sum < abs_S:
        right += 1
    else:
        left += 1

print(answer)

