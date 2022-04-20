from copy import deepcopy
import sys
input = sys.stdin.readline
def to_left(graph_arg):
    new_nums = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph_arg[i][j] == 0: # 0이면 지나가기
                continue
            now_val = graph_arg[i][j]
            find_flag = False
            for k in range(j + 1, N): # 다음 대상부터 순차 탐색
                if now_val == graph_arg[i][k]:
                    graph_arg[i][k] = 0
                    new_nums[i].append(now_val * 2) # 합해진 값 기록
                    find_flag = True
                    break
                elif graph_arg[i][k] != 0: # 합해질 수 없는 값이면
                    break # 어차피 이제 못 합치므로 break
            
            if not find_flag: # 합할 값 못 찾았으면
                new_nums[i].append(now_val) # 값 그대로 기록
    
    for i in range(N):
        cut = len(new_nums[i])
        for j in range(N - cut): # 빈 자리만큼 0 채우기
            new_nums[i].append(0)
        for j in range(N):
            graph_arg[i][j] = new_nums[i][j] # 새 값으로 바꿔주기
                
                
def to_right(graph_arg):
    new_nums = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N - 1, -1, -1): # 우 -> 좌로 확인하므로 거꾸로 탐색
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


def to_up(graph_arg): # to_left와 달리 열을 기준으로 행 탐색
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
            
            
def to_down(graph_arg): # to_up 순서 거꾸로 탐색
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