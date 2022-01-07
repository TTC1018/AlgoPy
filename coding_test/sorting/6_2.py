def quick_sort(num_list):
    if len(num_list) <= 1:
        return num_list

    pivot = num_list[0]

    rest = num_list[1:]

    left = [n for n in rest if n < pivot]
    right = [n for n in rest if n > pivot]

    return quick_sort(right) + [pivot] + quick_sort(left)


N = int(input())
nums = []

for i in range(N):
    nums.append(int(input()))

# 라이브러리 사용
nums.sort(reverse=True)
print(nums)

# 퀵 정렬
print(quick_sort(nums))

# 선택 정렬
for i in range(N):
    max_index = i
    for j in range(i + 1, N):
        if nums[j] > nums[max_index]:
            max_index = j
    nums[i], nums[max_index] = nums[max_index], nums[i]
print(nums)

# 삽입 정렬
for i in range(1, len(nums)):
    for j in range(i, 0, -1):
        if nums[j] > nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
        else:
            break
print(nums)


# 계수 정렬
max_val = max(nums)
counter = [0] * (max_val + 1)
for i in range(N):
    counter[nums[i]] += 1
for i in range(max_val, 0, -1):
    for j in range(counter[i]):
        print(i, end = ' ')
