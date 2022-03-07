def find_parent(node):
    if parent[node] != node:
        return find_parent(parent[node])
    return parent[node]


loop = int(input())
parent = []
for _ in range(loop):
    n = int(input())
    t = [0] + list(map(int, input().split()))
    rank = dict()
    for i in range(1, n + 1):
        rank[t[i]] = i
    parent = [0, 1] + [n for n in range(1, n)]

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if rank[a] > rank[b]:
            parent[rank[a]] = rank[b]
        else:
            parent[rank[b]] = rank[a]
    # 올해 순위 오름차순으로, 확실하지 않은 순위는 ?
    # 순위를 정할 수 없으면 IMPOSSIBLE
    answer = []
    for i in range(1, n + 1):
        # 상위 찾기
        high_count, low_count = 0, 0
        for j in [k for k in range(1, n + 1) if k != i]:
            if find_parent(j) < i:
                high_count += 1
            else:
                low_count += 1
        if high_count + low_count == n - 1:
            answer.append(rank[i])
        else:
            answer.append('?')
    print(parent)
    if answer.count('?') == n:
        print('IMPOSSIBLE')
    else:
        print(*answer)



