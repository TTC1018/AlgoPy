from collections import deque

N = int(input())
M = int(input())

m = [[] for n in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    m[a].append(b)
    m[b].append(a)
visited = [-1] * (N + 1)

q = deque()
q.append(1)
visited[1] = 1

answer = 0
while q:
    now = q.popleft()

    for next in m[now]:
        if visited[next] == -1:
            visited[next] = 1
            answer += 1
            q.append(next)

print(answer)