from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)
order = list(map(int, input().split()))
if order[0] != 1:
    print(0)
    sys.exit()

ref = [0] * N
for idx in range(N):
    ref[order[idx] - 1] = idx
for g in graph:
    g.sort(key=lambda x:ref[x])
    # 다양한 답이 나올 수 있으므로
    # 제시하는 순서에 맞는 답을 출력하도록 정렬

visited = [False] * N
visited[0] = True
q = deque()    
q.append(0)
answer = []
while q:
    now = q.popleft()
    answer.append(now + 1)
    
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)
            
if answer == order:
    print(1)
else:
    print(0)