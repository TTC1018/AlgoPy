from itertools import permutations

N = int(input())
nums = [n for n in input().split(' ')]
answer = 0
for i in range(N-1):
    answer += abs(int(nums[i]) - int(nums[i+1]))

per = [list(map(int, list(l))) for l in list(permutations(nums))]
for l in per:
    sum = 0
    for i in range(len(l)-1):
        sum += abs(l[i] - l[i+1])
    answer = max(answer, sum)

print(answer)