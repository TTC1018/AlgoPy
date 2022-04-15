import sys
input = sys.stdin.readline


def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


G = int(input())
P = int(input())
parent = [i for i in range(G + 1)]

answer = 0
for _ in range(P):
    limit = int(input())
    if find_parent(limit) != 0:
        answer += 1
        empty_gate = find_parent(limit)
        union_parent(empty_gate, empty_gate - 1)
    else:
        break
print(answer)