import sys
input = sys.stdin.readline


def generate_tree(start, end, idx):
    if start == end:
        s_tree[idx] = A[start]
        return s_tree[idx]

    mid = (start + end) // 2
    s_tree[idx] = min(generate_tree(start, mid, idx * 2), generate_tree(mid + 1, end, idx * 2 + 1))
    return s_tree[idx]


def search(ns, ne, ts, te, idx):
    if ns > te or ne < ts:
        return int(1e9)
    if ts <= ns and ne <= te:
        return s_tree[idx]

    mid = (ns + ne) // 2
    return min(search(ns, mid, ts, te, idx * 2), search(mid + 1, ne, ts, te, idx * 2 + 1))


def update(start, end, node, new, idx):
    if start <= node <= end:
        if start == end:
            s_tree[idx] = new
            return s_tree[idx]

        mid = (start + end) // 2
        left = update(start, mid, node, new, idx * 2)
        right = update(mid + 1, end, node, new, idx * 2 + 1)
        s_tree[idx] = min(left, right)
    return s_tree[idx]


N = int(input())
A = list(map(int, input().split()))
s_tree = [0] * (N * 4)
generate_tree(0, N - 1, 1)

answer = []
for _ in range(int(input())):
    op, x, y = map(int, input().split())
    x -= 1
    if op == 1:
        update(0, N - 1, x, y, 1)
        A[x] = y
    elif op == 2:
        y -= 1
        answer.append(search(0, N - 1, x, y, 1))
print('\n'.join(map(str, answer)))