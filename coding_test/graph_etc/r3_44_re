from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def find_parent(node):
    if parent[node] == node:
        return node
    
    parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


N = int(input())
dist = [[], [], []]
for i in range(N):
    X, Y, Z = map(int, input().split())
    dist[0].append((X, i))
    dist[1].append((Y, i))
    dist[2].append((Z, i))

parent = [i for i in range(N)]
edges = []
dist[0].sort()
dist[1].sort()
dist[2].sort()

for i in range(N - 1):
    for j in range(3):
        heappush(edges, (abs(dist[j][i][0] - dist[j][i + 1][0]), dist[j][i][1], dist[j][i + 1][1]))
        
answer = 0
while edges:
    cost, a, b = heappop(edges)
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += cost
print(answer)