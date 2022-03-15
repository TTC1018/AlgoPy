def t_check():
    result = True
    for tx, ty in t_loc:
        # 열 탐색
        for i in range(ty - 1, -1, -1):  # 열 좌측으로 탐색
            if graph[tx][i] == 'O':
                break
            elif graph[tx][i] == 'S':
                return False
        for i in range(ty + 1, N):  # 열 우측으로 탐색
            if graph[tx][i] == 'O':
                break
            elif graph[tx][i] == 'S':
                return False
        # 행 탐색
        for i in range(tx - 1, -1, -1):  # 행 위로 탐색
            if graph[i][ty] == 'O':
                break
            elif graph[i][ty] == 'S':
                return False
        for i in range(tx + 1, N):  # 행 아래로 탐색
            if graph[i][ty] == 'O':
                break
            elif graph[i][ty] == 'S':
                return False
    return result


def dfs(o_count):
    global answer

    if o_count == 3:
        if t_check():
            answer = 'YES'
        return

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                dfs(o_count + 1)
                graph[i][j] = 'X'


N = int(input())
graph = []

t_loc = []
for i in range(N):
    row = input().split()
    for j in range(N):
        if row[j] == 'T':
            t_loc.append((i, j))
    graph.append(row)

answer = 'NO'
dfs(0)
print(answer)
