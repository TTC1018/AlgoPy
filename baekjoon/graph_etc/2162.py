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

    if pa < pb:
        parent[pb] = pa
        p_cnt[pa] += p_cnt[pb]
        p_cnt[pb] = 0
    elif pa > pb:
        parent[pa] = pb
        p_cnt[pb] += p_cnt[pa]
        p_cnt[pa] = 0


# https://jason9319.tistory.com/358
def ccw(p1, p2, p3):
    op = (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p1[1]*p2[0] + p2[1]*p3[0] + p3[1]*p1[0])
    if op > 0:
        return 1
    elif op == 0:
        return 0
    else:
        return -1


# https://onecoke.tistory.com/entry/BOJ-%EB%B0%B1%EC%A4%80-2162-%EC%84%A0%EB%B6%84-%EA%B7%B8%EB%A3%B9-%EC%84%A0%EB%B6%84-%EA%B5%90%EC%B0%A8
def is_intersect(a, b):
    p1, p2 = a
    p3, p4 = b

    op1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    op2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    if op1 == 0 and op2 == 0:
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3
        return p1 <= p4 and p3 <= p2
    return op1 <= 0 and op2 <= 0


N = int(input())
parent = [i for i in range(N)]
p_cnt = [1 for _ in range(N)]

if N == 1:
    print(1)
    print(1)
else:
    lines = []
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        lines.append(((x1, y1), (x2, y2)))

    for i in range(N):
        for j in range(i + 1, N):
            if is_intersect(lines[i], lines[j]):
                union_parent(i, j)

    answer1 = 0
    answer2 = max(p_cnt)
    for i in range(N):
        temp_p = find_parent(i)
        if p_cnt[temp_p] > 0:
            answer1 += 1
            p_cnt[temp_p] = 0
    print(answer1)
    print(answer2)