from copy import deepcopy
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


def fill(grp_arg, cand, x, y):
    for d in cand:
        nx, ny = x, y
        while True:
            nx, ny = nx + direc[d][0], ny + direc[d][1]
            if in_range(nx, ny):
                if grp_arg[nx][ny] == 6:
                    break
                elif not grp_arg[nx][ny]:
                    grp_arg[nx][ny] = -1


def dfs(grp_arg, count):
    global answer

    if count == limit:
        result = 0
        for cand in range(N):
            for j in range(M):
                if grp_arg[cand][j] == 0:
                    result += 1
        answer = min(answer, result)
        return


    num, x, y = cctv[count]
    grp_cpy = deepcopy(grp_arg)
    for cand in cctv_direc[num]:
        fill(grp_cpy, cand, x, y)
        dfs(grp_cpy, count + 1)
        grp_cpy = deepcopy(grp_arg)

  
direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
limit = 0    
N, M = map(int, input().split())
cctv = []
graph = []
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(M):
        if 1 <= data[j] <= 5:
            cctv.append([data[j], i, j])
            limit += 1
    graph.append(data)
    
cctv_direc = [
    -1,
    [[i] for i in range(4)],
    [[i, i + 2] for i in range(2)],
    [[i, i - 1] for i in range(4)],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[i for i in range(4)]],
]



answer = int(1e9)
dfs(graph, 0)
print(answer)