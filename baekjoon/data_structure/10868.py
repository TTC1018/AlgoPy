import sys
input = sys.stdin.readline


def generate_tree(start, end, idx):
    if start == end:
        s_tree[idx] = nums[start]
        return s_tree[idx]

    mid = (start + end) // 2
    s_tree[idx] = min(generate_tree(start, mid, idx * 2), generate_tree(mid + 1, end, idx * 2 + 1))
    return s_tree[idx]

def search(now_s, now_e, start, end, idx):
    if end < now_s or start > now_e:
        return int(1e9)
    if start <= now_s and now_e <= end:
        return s_tree[idx]

    mid = (now_s + now_e) // 2
    return min(search(now_s, mid, start, end, idx * 2), search(mid + 1, now_e, start, end, idx * 2 + 1))


N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
s_tree = [0] * (N * 4)
generate_tree(0, N - 1, 1)

answer = []
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    answer.append(search(0, N - 1, a, b, 1))
print('\n'.join(map(str, answer)))