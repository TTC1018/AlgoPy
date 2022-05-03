from copy import deepcopy
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < 10 and 0 <= y < 10
INF = int(1e9)


def isFinished(grp_arg):
    for i in range(10):
        for j in range(10):
            if grp_arg[i][j] == 'O':
                return False
    return True


direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def switch(pos, grp_arg):
    x, y = pos
    grp_arg[x][y] = '#' if grp_arg[x][y] == 'O' else 'O' # 중앙 변경
    for d in direc: # 상하좌우 변경
        nx, ny = x + d[0], y + d[1]
        if in_range(nx, ny):
            grp_arg[nx][ny] = '#' if grp_arg[nx][ny] == 'O' else 'O'


graph = [list(input()) for _ in range(10)]
answer = INF
for i in range(1 << 10): # 첫줄의 경우의 수를 비트마스킹으로 표현
    count = 0 # 스위치 누른 횟수 기록
    tmp_graph = deepcopy(graph)
    for j in range(10):
        if 1 << j & i: # 스위치 누르는 경우면
            count += 1
            switch((0, j), tmp_graph) # 변경
    
    # 첫번째 줄을 기준으로 두번째 줄부터 체크 (지나간 줄은 되돌아오지 못하기 때문에)
    for j in range(1, 10):
        for k in range(10):
            if tmp_graph[j - 1][k] == 'O': # 켜져 있으면
                count += 1
                switch((j, k), tmp_graph) # 내 스위치를 눌러서 이전 줄을 꺼주기
    
    if isFinished(tmp_graph):
        answer = min(answer, count)

if answer != INF:
    print(answer)
else:
    print(-1)