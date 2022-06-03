import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(num):
    if not graph[num]: # 트리 끝이면
        return ws[num] if ws[num] > 0 else 0 # 늑대는 움직이지 못 하므로 셀 필요 없음

    s_cnt = ws[num]
    for nxt in graph[num]:
        s_cnt += dfs(nxt)

    return s_cnt if s_cnt > 0 else 0


N = int(input())
graph = [[] for _ in range(N + 1)]
ws = [0] * (N + 1)
for i in range(2, N + 1):
    t, a, p = input().split()
    a, p = int(a), int(p)
    graph[p].append(i)
    ws[i] = a if t == 'S' else -a

answer = dfs(1)
print(answer)