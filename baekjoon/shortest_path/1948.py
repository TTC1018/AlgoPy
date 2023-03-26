from collections import deque
import sys
input = sys.stdin.readline


def topology():
    q = deque([start])

    while q:
        now = q.popleft()
        for nxt, cost in graph[now]:
            result[nxt] = max(result[nxt], result[now] + cost)
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    answer = 0
    q.append(dest)
    while q:
        now = q.popleft()
        for prv, cost in graph_r[now]:
            if result[now] == result[prv] + cost: # 최대 시간을 갱신 시킨 지점
                answer += 1
                if not visited[prv]:
                    visited[prv] = True
                    q.append(prv)

    print(f'{result[dest]}\n{answer}', end='')

# n : 도시의 개수, m : 도로의 개수
n, m = int(input()), int(input())
graph = [[] * (n + 1) for _ in range(n + 1)]
graph_r = [[] * (n + 1) for _ in range(n + 1)]
indegree = [0] * (n + 1)  # 진입차수
visited = [False] * (n + 1)  # 백트래킹시 큐에 중복 삽입 방지
result = [0] * (n + 1)  # 각 도시로 이동하는 임계 경로 저장을 위한 변수
for _ in range(m):
    s, d, cost = map(int, input().split())
    graph[s].append((d, cost))
    graph_r[d].append((s, cost))
    indegree[d] += 1

start, dest = map(int, input().split())
topology()
