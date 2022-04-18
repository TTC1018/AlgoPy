import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000) # 백준 recursionError 방지


def find_parent(x, y):
    if parent[x][y] != (x, y):
        px, py = parent[x][y]
        parent[x][y] = find_parent(px, py)
    return parent[x][y]


def union_parent(a, b):
    pa = find_parent(a[0], a[1])
    pb = find_parent(b[0], b[1])
    
    if pa != pb:
        ax, ay = pa
        bx, by = pb
        
        parent[bx][by] = pa
        p_check[ax][ay] += p_check[bx][by]
        p_check[bx][by] = 0


direc = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}
def move_to_end(start):
    x, y = start
    now = graph[x][y]
    
    q = deque()
    q.append(((x, y), now))
    while q:
        pos, op = q.popleft()
        nx, ny = pos[0] + direc[op][0], pos[1] + direc[op][1]
        union_parent(start, (nx, ny))
        
        # union 후에 visited 체크해야 빠짐없이 + 중복없이 탐색됨
        # 바로 visited 체크하면 합집합 안 되는 경우 생김
        if not visited[nx][ny]: 
            q.append(((nx, ny), graph[nx][ny]))
            visited[nx][ny] = True
    

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
parent = [[(i, j) for j in range(M)] for i in range(N)]
visited = [[False] * M for _ in range(N)]
p_check = [[1] * M for _ in range(N)] # 자신을 부모로 하는 노드 개수 기록

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            move_to_end((i, j)) # 같은 집합 쫙 처리

answer = 0
for i in range(N):
    for j in range(M):
        px, py = find_parent(i, j)
        if p_check[px][py] > 0:
            p_check[px][py] = 0
            answer += 1
print(answer)