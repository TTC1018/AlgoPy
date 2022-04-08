info_list = []
childs = []
answer = 0
visited = []


def dfs(now, sheep, wolf, nexts):
    global info_list, answer, visited

    if info_list[now] == 0:  # 양일 때
        sheep += 1
        answer = max(answer, sheep)
    else:
        wolf += 1

    if sheep <= wolf:  # 늑대 수가 양 이상이 됐을 때
        return

    nexts.extend(childs[now])
    for next in nexts:
        visited[next] = True
        dfs(next, sheep, wolf, [n for n in nexts if n != next and not visited[n]])
        visited[next] = False


def solution(info, edges):
    global info_list, childs, visited
    info_list = info
    childs = [[] for _ in range(len(info))]
    for e in edges:
        p, c = e
        childs[p].append(c)

    visited = [False] * len(info)
    visited[0] = True
    dfs(0, 0, 0, [])

    return answer
