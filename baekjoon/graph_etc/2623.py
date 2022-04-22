from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    data = list(map(int, input().split()))
    d_len = data[0]
    for i in range(1, d_len + 1):
        for j in range(i + 1, d_len + 1):
            graph[data[i]].append(data[j])
            indegree[data[j]] += 1

q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

answer = []
while q:
    now = q.popleft()
    answer.append(now)
    
    for n in graph[now]:
        indegree[n] -= 1
        if indegree[n] == 0:
            q.append(n)

if len(answer) == N:
    print(*answer)
else:
    print(0)