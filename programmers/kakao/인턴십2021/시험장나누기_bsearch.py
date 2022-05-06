import sys
sys.setrecursionlimit(100000)


n = 0
g_num = 0
root = 0
child, parent, capa = [], [], []


def dfs(now, limit):
    global g_num
    lv, rv = 0, 0
    if child[now][0] != -1:
        lv = dfs(child[now][0], limit)
    if child[now][1] != -1:
        rv = dfs(child[now][1], limit)
    
    if capa[now] + lv + rv <= limit:
        return capa[now] + lv + rv # 한 그룹으로 올라가기
    if capa[now] + min(lv, rv) <= limit:
        g_num += 1 # 하나는 따로 그룹으로 만들기 (버리기)
        return capa[now] + min(lv, rv)

    g_num += 2 # 자식들은 다 따로 그룹으로 만들기 (자식 다 버리기)
    return capa[now]


def is_ok(limit):
    global g_num
    g_num = 0
    dfs(root, limit)
    g_num += 1 # 마지막에 결성된 그룹
    return g_num


def solution(k, num, links):
    global n, parent, child, capa, root
    
    n = len(num)
    parent = [-1] * n
    child = [[-1, -1] for _ in range(n)]
    capa = num
    
    for i in range(n):
        lc, rc = links[i]
        if lc != -1:
            parent[lc] = i
        if rc != -1:
            parent[rc] = i
        child[i] = lc, rc
    
    # 루트 노드 찾기
    for i in range(n):
        if parent[i] == -1:
            root = i
            break
    
    # lower bound 이분탐색으로 가능한 최대 그룹 인원 최솟값 찾기
    answer = 0
    start, end = max(capa), 10**8
    while start <= end:
        mid = (start + end) // 2
        if is_ok(mid) <= k:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    return answer