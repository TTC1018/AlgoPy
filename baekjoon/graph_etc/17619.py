import sys
input = sys.stdin.readline


def find_parent(node):
    if parent[node] == node:
        return node

    parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa != pb:
        parent[pb] = pa


N, Q = map(int, input().split())
parent = [i for i in range(N)]

logs = []
for i in range(N):
    x1, x2, y = map(int, input().split())
    logs.append((x1, x2, i)) # x좌표 순으로 정렬할 것이기 때문에 인덱스 저장해둠
logs.sort(key=lambda x: (x[0], x[1]))

px, py, _ = logs[0]
for i in range(1, N):
    nx, ny, _ = logs[i]
    if nx <= py: # 길이 순으로 정렬됐기 때문에, 이전 통나무 끝 vs 다음 통나무 처음만 비교
        union_parent(logs[i - 1][2], logs[i][2]) # 겹치면 합집합
        py = max(py, ny) # 이전 좌표가 더 길 수도 있으니 고려해서 갱신
    else:
        px, py = nx, ny

for _ in range(Q):
    a, b = map(int, input().split())
    if find_parent(a - 1) == find_parent(b - 1):
        print(1)
    else:
        print(0)
