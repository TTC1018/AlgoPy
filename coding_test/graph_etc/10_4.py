from collections import deque
import copy


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0: # 진입차수 0인 노드부터 시작
            q.append(i)

    while q:
        now = q.popleft()
        for next in graph[now]:
            result[next] = max(result[next], result[now] + time[next])
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    for i in range(1, N + 1):
        print(result[i])


N = int(input())
indegree = [0] * (N + 1) # 진입차수 리스트
graph = [[] for _ in range(N + 1)] # 간선 정보 리스트
time = [0] * (N + 1) # 강의 시간 리스트

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for rest in data[1:-1]:
        indegree[i] += 1
        graph[rest].append(i)

topology_sort()