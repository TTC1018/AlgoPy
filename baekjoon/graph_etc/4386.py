from heapq import heappush, heappop
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


n = int(input())
parent = [i for i in range(n + 1)]
points = []
for _ in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

edges = []
for i in range(n):
    p1 = points[i]
    for j in range(i + 1, n):
        p2 = points[j]
        dist = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)
        heappush(edges, (dist, i, j))

count = 0
answer = 0
while edges:
    if count == n - 1:
        break

    dist, i, j = heappop(edges)
    if find_parent(i) != find_parent(j):
        union_parent(i, j)
        answer += dist
        count += 1
print('{0:.2f}'.format(answer))