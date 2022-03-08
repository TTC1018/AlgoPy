from collections import deque

for _ in range(int(input())):
    n = int(input())
    indegree = [0] * (n + 1)  # 진입 차수
    graph = [[False] * (n + 1) for i in range(n + 1)]  # 연결 여부

    rank = list(map(int, input().split()))
    for i in range(n):
        for j in range(i + 1, n):
            graph[rank[i]][rank[j]] = True
            indegree[rank[j]] += 1  # 진입 차수 상승

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b], graph[b][a] = False, True  # 간선 방향을 거꾸로 변경
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b], graph[b][a] = True, False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:  # 진입 차수 0 = 위상 정렬 시작 지점
            q.append(i)

    onlyOne = True
    isCycle = False

    for i in range(n):
        if len(q) == 0:  # 다 확인하기 전에 큐가 빈 경우 = 싸이클
            isCycle = True
            break

        if len(q) >= 2:  # 큐에 답이 두개 이상 있는 경우 = 위상 정렬의 값이 여러개 존재
            onlyOne = False
            break

        now = q.popleft()
        result.append(now)
        for j in range(1, n + 1):
            if graph[now][j]:  # 연결 돼있는 간선
                indegree[j] -= 1  # 진입 차수 내리고
                if indegree[j] == 0:  # 진입 차수 0이면 큐에 추가
                    q.append(j)

    if isCycle:
        print('IMPOSSIBLE')
    elif not onlyOne:
        print('?')
    else:
        print(*result)