import sys
from copy import deepcopy
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
    if A[pa] < A[pb]:
        parent[pb] = pa
    else:
        parent[pa] = pb


N, M, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
parent = [i for i in range(N + 1)]
for _ in range(M):
    v, w = map(int, input().split())
    union_parent(v, w)
    
answer = 0
for i in range(1, N + 1):
    target = find_parent(i)
    if target != 0:
        answer += A[target]
        union_parent(0, target) # 방문처리

if answer > k:
    print("Oh no")
else:
    print(answer)