import sys
sys.setrecursionlimit(10**6)
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

for _ in range(m):
    func, a, b = map(int, input().split())
    
    if func == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")