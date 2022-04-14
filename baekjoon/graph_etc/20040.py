import sys
input = sys.stdin.readline

def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    
    if pa == pb:
        return
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

answer = 0
for i in range(m):
    a, b = map(int, input().split())
    if answer == 0:
        if find_parent(a) == find_parent(b):    
            answer = i + 1
        union_parent(a, b)
   
print(answer)