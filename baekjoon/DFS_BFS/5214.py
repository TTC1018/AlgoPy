from collections import deque
import sys
input = sys.stdin.readline


N, K, M = map(int, input().split())
route = [[] for _ in range(N + M + 1)]
for i in range(1, M + 1):
    station = list(map(int, input().split()))
    for j in range(K):
        route[station[j]].append(N + i)
        route[N + i].append(station[j])


visited = [False] * (N + M + 1)
visited[1] = True
q = deque()
q.append((1, 0))
answer = -1
while q:
    now, cnt = q.popleft()

    if now == N:
        answer = cnt // 2 + 1 # 역 -> 역 이 아니라 역 -> 튜브 -> 역으로 카운트 했기 때문에
        break

    for nxt in route[now]:
        if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, cnt + 1))
print(answer)