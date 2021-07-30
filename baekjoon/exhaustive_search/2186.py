from collections import deque

N, M, K = [int(n) for n in input().split(' ')]
alphas = []
for i in range(N):
    alphas.append(list(input()))

target = input()
q = deque()

for i in range(N):
    for j in range(M):
        if alphas[i][j] == target[0]:
            q.append(([(i, j)], target[0]))

answer = []
while q:
    points, word = q.popleft()
    if word == target and points not in answer:
        answer.append(points)

    x, y = points[-1]
    for i in range(K):
        




print(len(answer))
