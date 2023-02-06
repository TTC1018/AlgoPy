import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def generate_tree(start, end, idx):
    if start == end:
        s_tree[idx] = nums[start]
        return s_tree[idx]

    mid = (start + end) // 2
    s_tree[idx] = generate_tree(start, mid, idx * 2) + generate_tree(mid + 1, end, idx * 2 + 1)
    return s_tree[idx]


def range_sum(ns, ne, ts, te, idx):
    if ne < ts or ns > te:
        return 0
    if ts <= ns and ne <= te:
        return s_tree[idx]

    mid = (ns + ne) // 2
    return range_sum(ns, mid, ts, te, idx * 2) + range_sum(mid + 1, ne, ts, te, idx * 2 + 1)


def update(start, end, node, diff, idx):
    if start <= node <= end:
        s_tree[idx] += diff
        if start != end:
            mid = (start + end) // 2
            update(start, mid, node, diff, idx * 2)
            update(mid + 1, end, node, diff, idx * 2 + 1)


N, Q = map(int, input().split())
nums = list(map(int, input().split()))
s_tree = [0] * (N * 4)
generate_tree(0, N - 1, 1)


answer = []
for _ in range(Q):
    x, y, a, b = map(lambda x: int(x) - 1, input().split())
    b += 1
    if x > y:
        x, y = y, x
    answer.append(str(range_sum(0, N - 1, x, y, 1)))
    update(0, N - 1, a, b - nums[a], 1)
    nums[a] = b
print('\n'.join(answer))