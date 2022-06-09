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
    if pa != pb:
        parent[pb] = pa


N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
parent = [i for i in range(N * M)]
d_dict = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

for i in range(N):
    for j in range(M):
        now = i * M + j
        direc = graph[i][j]
        nxt = (i + d_dict[direc][0]) * M + (j + d_dict[direc][1])
        union_parent(now, nxt)

answer = set()
for i in range(N):
    for j in range(M):
        answer.add(find_parent(i * M + j))
print(len(answer))