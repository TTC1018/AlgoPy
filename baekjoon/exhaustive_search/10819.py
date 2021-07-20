# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]| 의 최댓값 구하기
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


N = int(input())
nums = [int(''.join(n)) for n in input().split(' ')]
answer = 0
for i in range(len(nums) - 1):
        answer += abs(nums[i] - nums[i + 1])

per = permute(nums)
for list in per:
    sum = 0
    for i in range(len(list) - 1):
        sum += abs(list[i] - list[i + 1])
    answer = max(answer, sum)

print(answer)