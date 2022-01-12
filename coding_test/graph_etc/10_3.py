def find_parent(x):
    if p_list[x] != x:
        return find_parent(p_list[x])
    return p_list[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        p_list[a] = b
    else:
        p_list[b] = a


N, M = map(int, input().split())
p_list = [i for i in range(N + 1)]

edges = []
cost = 0
for i in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
erase = 0 # 제거 대상 간선

for e in edges:
    C, A, B = e
    if find_parent(A) != find_parent(B): # 사이클 없는 경우
        union_parent(A, B)
        cost += C
        erase = C # for 문이 끝나면 가장 큰 값의 간선이 저장됨

print(cost - erase)