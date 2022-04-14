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

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
T = list(map(int, input().split()))
answer = 0
if T[0] == 0:
    answer = M
    for _ in range(M):
        data = map(int, input().split())
else:
    for i in range(2, T[0] + 1):
        union_parent(T[1], T[i])
    
    party = []
    for _ in range(M):
        data = list(map(int, input().split()))
        for j in range(2, data[0] + 1):
            union_parent(data[1], data[j])
        party.append(data[1])
    
    to_evade = find_parent(T[1])
    for p in party:
        if find_parent(p) != to_evade:
            answer += 1
print(answer)
# 지민이는 모든 파티에 참여
# 진실을 아는 사람이 포함된 파티에 참여하면
# 그 인원이 참여하지 않은 파티에만 참여 가능
# => 진실을 아는 사람이 포함된 파티에 참여한 사람은 parent 일치시킴