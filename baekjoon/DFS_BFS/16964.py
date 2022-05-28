import sys
input = sys.stdin.readline


def dfs(num):
    global answer
    if visited[num]:
        return
    visited[num] = True
    answer.append(num + 1)
    
    for nxt in graph[num]:
        if not visited[nxt]:
            dfs(nxt)


N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
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
    # 정답이 여러개가 가능하므로
    # 제시하는 순서에 맞게 간선을 정렬해야함

visited = [False] * N
answer = []
dfs(order[0] - 1)
if answer == order:
    print(1)
else:
    print(0)