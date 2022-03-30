import heapq


INF = int(1e9)
N, M = int(input()), int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s_num, e_num, cost = map(int, input().split())
    graph[s_num].append((e_num, cost))
    
start, end = map(int, input().split())
distance = [INF] * (N + 1)
distance[start] = 0

q = []
while q:
    pass