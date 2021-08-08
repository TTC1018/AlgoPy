from collections import deque
from itertools import combinations

N, S = tuple(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))

q = deque()
for n in nums:
    q.append((n, ))

answer = []
for i in range(1, len(nums) + 1):
    candidate = combinations(nums, i)
    for c in candidate:
        if sum(c) == S:
            answer.append(c)


print(len(answer))