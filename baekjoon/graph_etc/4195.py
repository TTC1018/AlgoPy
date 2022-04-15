from collections import defaultdict
import sys
input = sys.stdin.readline


def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    
    if pa != pb: # 둘 중에 하나가 부모가 되기만 하면 되므로, 아무나 부모로 설정한다.
        parent[pb] = pa
        p_cnt[pa] += p_cnt[pb]
        

for _ in range(int(input())):
    F = int(input())
    parent = dict()
    p_cnt = defaultdict(int)
    
    for _ in range(F):
        a, b = input().split()
        if not parent.get(a):
            parent[a] = a
            p_cnt[a] += 1
        if not parent.get(b):
            parent[b] = b
            p_cnt[b] += 1
        union_parent(a, b)
        print(p_cnt[find_parent(a)])