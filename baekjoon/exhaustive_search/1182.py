from collections import deque

N, S = tuple(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))

q = deque()
for n in nums:
    q.append([n])

answer = set()
while q:
    x = q.popleft()

    if sum(x) == S and x not in answer:
        answer.add(x)
        continue

    for n in nums:
        if n not in x:
            q.append(x + [n])

print(len(answer))