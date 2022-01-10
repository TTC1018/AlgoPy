import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

start = int(input())
graph = [[] for i in range(N + 1)] # 경로 그래프
distance = [INF] * (N + 1) # 최단거리 값 저장 리스트

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a -> b 의 거리값이 c임을 의미

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 방문했거나 (최단거리값이 INF가 아니거나) 계산해봤자 최단거리가 아닌 경우
            continue
        for i in graph[now]: # 노드now와 연결된 노드 간의 거리 순차 확인
            cost = dist + i[1] # 새로운 거리
            if cost < distance[i[0]]: # 기존 최단거리보다 짧을 경우
                distance[i[0]] = cost # 최단거리 교체
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])