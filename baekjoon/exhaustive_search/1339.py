N = int(input())
nums = []

for i in range(N):
    nums.append(list(input()))


max_len = len(nums[0])
starts = [nums[0]]
for n in nums:
    if n != nums[0]:
        if len(n) == max_len:
            starts.append(n)
        else:
            break


def solve(num_list, vals, next_max, result):
    for n in num_list:
        i = len(n)
        for alpha in n:
            idx = ord(alpha) - 65
            if vals[idx] == -1:
                vals[idx] = next_max
                next_max -= 1
            result += (vals[idx] * 10 ** (i - 1))
            i -= 1

    return result


answer = 0
for s in starts:
    vals = [-1] * 10
    max_temp = 9
    for alpha in s:
        if vals[ord(alpha) - 65] == -1:
            vals[ord(alpha) - 65] = max_temp
        max_temp -= 1
    result = solve(nums, vals, max_temp, 0)
    answer = max(answer, result)
print(answer)