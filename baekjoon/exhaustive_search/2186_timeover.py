from collections import deque

N, M, K = [int(n) for n in input().split(' ')]
alphas = []
for i in range(N):
    alphas.append(input())
target = input()

q = deque()
for idx, l in enumerate(alphas):
    if target[0] in l:
        q.append([[idx, l.index(target[0])], 1])

answer = 0
t_len = len(target)
while q:
    point, count = q.popleft()

    if count == t_len:
        answer += 1
        continue

    x, y = point
    for i in range(x-K, x+K + 1):
        if 0 <= i <= N-1:
            if alphas[i][y] == target[count]:
                q.append([[i, y], count + 1])

    for i in range(y-K, y+K + 1):
        if 0 <= i <= M-1:
            if alphas[x][i] == target[count]:
                q.append([[x, i], count + 1])


print(answer)