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
        p_cnt[pa] += p_cnt[pb]
        p_cnt[pb] = 0


N = int(input())
parent = [i for i in range(10**6 + 1)]
p_cnt = [1 for _ in range(10**6 + 1)]
for _ in range(N):
    data = input().split()
    type = data[0]

    if type == 'I':
        a, b = map(int, data[1:])
        union_parent(a, b)
    else:
        target = find_parent(int(data[1]))
        print(p_cnt[target])