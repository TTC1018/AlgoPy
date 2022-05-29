import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(node):
    global answer, farthest
    if visited[node] > answer:
        answer = visited[node]
        farthest = node
    
    for nxt, dist in graph[node]:
        if visited[nxt] == -1:
            visited[nxt] = visited[node] + dist
            dfs(nxt)
        

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(1, N + 1):
    data = list(map(int, input().split()))
    for j in range(1, len(data[1:]), 2):
        graph[data[0]].append(data[j:j+2])

# 트리 내 두 정점 간 경로는 항상 유일함
# 그리고 어떤 정점간 거리든
# 가장 먼 거리를 갖는 두 정점 간 경로와 겹칠 수 밖에 없음
# 그리고 어느 점에서 시작을 하든 가장 먼 거리의 도착점은 
# 가장 먼 거리를 갖는 두 정점 중에 하나임

answer = 0
farthest = 0

visited = [-1] * (N + 1)
visited[1] = 0
dfs(1) # 가장 먼 거리의 정점 중 하나 탐색

visited = [-1] * (N + 1)
visited[farthest] = 0
dfs(farthest) # 가장 먼 거리의 두 정점 중 하나에서 길이 측정
print(answer)