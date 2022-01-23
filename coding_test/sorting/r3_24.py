N = int(input())
nums = list(map(int, input().split()))
nums.sort()

start, end = 0, N - 1
answer = 200000 * 100000
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for n in nums:
        temp += abs(n - nums[mid])

    if answer < temp:
        break
    else:
        answer = nums[mid]
        end = mid - 1

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for n in nums:
        temp += abs(n - nums[mid])

    if answer < temp:
        break
    else:
        answer = nums[mid]
        start = mid + 1


print(answer)