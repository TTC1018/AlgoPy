from copy import deepcopy
import sys
input = sys.stdin.readline
def to_left(graph_arg):
    new_nums = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph_arg[i][j] == 0:
                continue
            now_val = graph_arg[i][j]
            find_flag = False
            for k in range(j + 1, N):
                if now_val == graph_arg[i][k]:
                    graph_arg[i][k] = 0
                    new_nums[i].append(now_val * 2)
                    find_flag = True
                    break
                elif graph_arg[i][k] != 0:
                    break
            
            if not find_flag:
                new_nums[i].append(now_val)
    
    for i in range(N):
        cut = len(new_nums[i])
        for j in range(N - cut):
            new_nums[i].append(0)
        for j in range(N):
            graph_arg[i][j] = new_nums[i][j]
                
                
def to_right(graph_arg):
    new_nums = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N - 1, -1, -1):
            if graph_arg[i][j] == 0:
                continue
            now_val = graph_arg[i][j]
            find_flag = False
            for k in range(j - 1, -1, -1):
                if now_val == graph_arg[i][k]:
                    graph_arg[i][k] = 0
                    new_nums[i].append(now_val * 2)
                    find_flag = True
                    break
                elif graph_arg[i][k] != 0:
                    break
            
            if not find_flag:
                new_nums[i].append(now_val)
    
    for i in range(N):
        cut = len(new_nums[i])
        for j in range(N - cut):
            new_nums[i].append(0)
        for j in range(N):
            graph_arg[i][N - 1 - j] = new_nums[i][j]


def to_up(graph_arg):
    new_nums = [[] for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if graph_arg[i][j] == 0:
                continue
            now_val = graph_arg[i][j]
            find_flag = False
            for k in range(i + 1, N):
                if now_val == graph_arg[k][j]:
                    graph_arg[k][j] = 0
                    new_nums[j].append(now_val * 2)
                    find_flag = True
                    break
                elif graph_arg[k][j] != 0:
                    break
            
            if not find_flag:
                new_nums[j].append(now_val)
    
    for i in range(N):
        cut = len(new_nums[i])
        for j in range(N - cut):
            new_nums[i].append(0)
        for j in range(N):
            graph_arg[j][i] = new_nums[i][j]
            
            
def to_down(graph_arg):
    new_nums = [[] for _ in range(N)]
    for j in range(N):
        for i in range(N - 1, -1, -1):
            if graph_arg[i][j] == 0:
                continue
            now_val = graph_arg[i][j]
            find_flag = False
            for k in range(i - 1, -1, -1):
                if now_val == graph_arg[k][j]:
                    graph_arg[k][j] = 0
                    new_nums[j].append(now_val * 2)
                    find_flag = True
                    break
                elif graph_arg[k][j] != 0:
                    break
            
            if not find_flag:
                new_nums[j].append(now_val)
    
    for i in range(N):
        cut = len(new_nums[i])
        for j in range(N - cut):
            new_nums[i].append(0)
        for j in range(N):
            graph_arg[N - 1 - j][i] = new_nums[i][j]


def search_max(graph_arg):
    max_val = 0
    for i in range(N):
        max_val = max(max_val, max(graph_arg[i]))
    return max_val


ops = [to_left, to_right, to_up, to_down]
def dfs(graph_arg, count):
    global answer
    
    if count == 5:
        answer = max(answer, search_max(graph_arg))
        return
    
    for i in range(4):
        temp_graph = deepcopy(graph_arg)
        ops[i](temp_graph)
        dfs(temp_graph, count + 1)
    
    
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dfs(graph, 0)
print(answer)