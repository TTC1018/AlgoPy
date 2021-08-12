from collections import deque

N, S = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

q = deque()
q.append((0, len(nums)))

answer = 0
while q:
    l, r = q.popleft()

    temp_sum = sum(nums[l:r])
    if temp_sum == S:
        answer += 1
        continue

    n_left = l + 1
    if n_left < r < len(nums):
        q.append((n_left, r))

    n_right = r - 1
    if 0 < l < n_right:
        q.append((l, n_right))



print(answer)

