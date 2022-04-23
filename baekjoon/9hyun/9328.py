for _ in range(int(input())):
    h, w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    key = list(input())
    key_dict = dict()
    for k in key:
        key_dict[k] = True

    for i in range(w):
        if graph[0][i] != '*':
            dfs()
        if graph[h - 1][i] != '*':
            dfs()
    for i in range(h):
        if graph[i][0] != '*':
            dfs()
        if graph[h - 1][0] != '*':
            dfs()