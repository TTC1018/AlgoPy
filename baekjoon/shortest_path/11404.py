import sys
input = sys.stdin.readline


INF = int(1e9)
n, m = int(input()), int(input())
distance = [[INF] * n for _ in range(n)]
for i in range(n):
    distance[i][i] = 0


for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if distance[a][b] > c:
        distance[a][b] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            new_dist = distance[i][k] + distance[k][j]
            if distance[i][j] > new_dist:
                distance[i][j] = new_dist

for i in range(n):
    for j in range(n):
        if distance[i][j] == INF:
            distance[i][j] = 0
for dist in distance:
    print(*dist)