from itertools import combinations
import sys
input = sys.stdin.readline


def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    
    if pa != pb:
        parent[pb] = pa


for _ in range(int(input())):
    N = int(input())
    parent = [i for i in range(N)]
    pos_inf = dict()
    for i in range(N):
        x, y, R = map(int, input().split())
        pos_inf[i] = (x, y, R)
    
    answer = N
    for i in range(N):
        for j in range(i + 1, N):
            ax, ay, aR = pos_inf[i]
            bx, by, bR = pos_inf[j]
            
            # 중심간의 거리와 반지름 합의 거리 비교
            center_dist = (ax - bx)**2 + (ay - by)**2
            radius_dist = (aR + bR)**2
                    
            if center_dist <= radius_dist:
                if find_parent(i) != find_parent(j):
                    union_parent(i, j)
                    answer -= 1 # 다른 영역에서 합쳐졌으므로 1 감소
    print(answer)