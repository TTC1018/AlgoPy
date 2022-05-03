from bisect import bisect_right
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
    else:
        parent[pa] = pb


N, M, K = map(int, input().split())
parent = [i for i in range(M + 1)]
blue = [-1] + list(map(int, input().split()))
blue.sort()

# 철수 - 모든 카드 사용 및 재사용 가능
# 민수 - 철수가 낼 카드보다 큰 것 중 가장 작은 수
R = list(map(int, input().split()))
for red in R:
    
    # red 초과하는 수 찾기
    target = red + 1
    t_start = bisect_right(blue, red + 1) - 1
    if t_start == 0: # 미사용 인덱스 union 방지
        t_start += 1
    
    # 가능한 최소값부터 탐색
    for i in range(t_start, M + 1):
        if find_parent(i) == i:
            target = blue[i]
            union_parent(i, i - 1) # 사용처리
            break
    print(target)