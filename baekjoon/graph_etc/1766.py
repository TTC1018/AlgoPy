from heapq import heappush, heappop
import sys
input = sys.stdin.readline
# 먼저 푸는 것이 좋은 문제가 있으면 무조건 먼저
# 가능하면 작은 번호 문제부터 풀기

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1
    
answer = []
q = []
for cand in [i for i in range(1, N + 1) if indegree[i] == 0]:
    heappush(q, cand)

while q:
    now = heappop(q)
    answer.append(now)
    
    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heappush(q, nxt)
print(*answer)