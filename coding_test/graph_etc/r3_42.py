def find_parent(node):
    if parent[node] != node:
        return find_parent(parent[node])
    return node


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa


G = int(input())
P = int(input())
parent = [i for i in range(G + 1)]

# 아이디어
# 도킹 가능한 곳중 최대값을 갖는 곳에 도킹하는 것이 후발 주자들에게 유리하다
# 도킹한 곳의 부모를 바로 왼쪽 위치로 설정한다
# 그러다가 부모가 0으로 설정되면 더이상 도킹 불가하다는 의미

answer = 0
for _ in range(P):
    available = find_parent(int(input()))
    if available == 0:
        break
    answer += 1
    union_parent(available, available - 1)
print(answer)