from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
in_range = lambda x, y: 1 <= x <= h and 1 <= y <= w


direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def dfs(pos):
    global answer

    x, y = pos
    for d in direc:
        nx, ny = x + d[0], y + d[1]
        if in_range(nx, ny):
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == '.':
                    dfs((nx, ny))
                elif graph[nx][ny] == '$':
                    answer += 1
                    dfs((nx, ny))
                elif graph[nx][ny] != '*':
                    if ord(graph[nx][ny]) >= 97: # 소문자 (새로운 열쇠)
                        key_dict[graph[nx][ny]] = True
                        new_key.append(graph[nx][ny])
                        dfs((nx, ny))
                    else: # 문
                        lowercase = chr(ord(graph[nx][ny]) + 32)
                        if key_dict.get(lowercase):
                            dfs((nx, ny))
                        else: # 아직 열 수 없는 방일 때
                            locked_door[lowercase].append((nx, ny))
                            # 나중에 갈 수 있을 때를 대비해서 위치 저장해두기


for _ in range(int(input())):
    h, w = map(int, input().split())
    graph = ['*' + input() + '*' for _ in range(h)] # 가장자리에 패딩처리
    graph.insert(0, '*' * w)
    graph.append('*' * w)
    
    key = input()
    key_dict = dict()
    if key != '0':
        for k in key:
            key_dict[k] = True
    locked_door = defaultdict(deque)
    new_key = deque()
    
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    answer = 0
    for i in range(w + 2):
        dfs((0, i))
        dfs((h + 1, i))
    for i in range(h + 2):
        dfs((i, 0))
        dfs((i, w + 1))
    
    # 열쇠 획득 후에 문 열리는지 확인
    while new_key:
        k = new_key.popleft()
        while locked_door[k]:
            x, y = locked_door[k].popleft()
            visited[x][y] = True
            dfs((x, y))
    
    print(answer)