def find_child(node):

    if len(child_candidate[node]) == 0:
        return 1
    else:
        for child in child_candidate[node]:
            child_count[node] += find_child(child)


N, M = map(int, input().split())
child_count = [0] * (N + 1)
child_candidate = [[] for _ in range(N + 1)]
parent_candidate = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    parent_candidate[x].append(y)
    child_candidate[y].append(x)

print(child_count)

answer = 0
for i in range(1, N + 1):
    find_child(i)
    if child_count[i] + len(parent_candidate[i]) == N:
        answer += 1
print(answer)