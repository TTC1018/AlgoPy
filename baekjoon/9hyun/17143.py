from collections import defaultdict
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < R and 0 <= y < C


def shark_move():
    next_shark = defaultdict(list)
    for s_num in s_info:
        pos, s, d, z = s_info[s_num]
        x, y = pos
        graph[x][y] = 0 # 원래 위치 비우기
        
        dx, dy = direc[d][0], direc[d][1]
        for _ in range(s):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny): 
                x, y = nx, ny
            else: # 벽일 때
                dx, dy = -dx, -dy
                x, y = x + dx, y + dy
                
        d = direc.index((dx, dy))
        s_info[s_num][2] = d # 방향 갱신
        next_shark[(x, y)].append(s_num)
    
    for pos_key in next_shark:
        if len(next_shark[pos_key]) > 1: # 한 공간에 여러마리
            biggest, size_val = 0, 0
            for s_num in next_shark[pos_key]:
                if s_info[s_num][3] > size_val:
                    size_val = s_info[s_num][3]
                    biggest = s_num            
            
            graph[pos_key[0]][pos_key[1]] = biggest
            s_info[biggest][0] = pos_key
            for removal in [s for s in next_shark[pos_key] if s != biggest]:
                s_info.pop(removal)
        else:
            s_num = next_shark[pos_key][0]
            graph[pos_key[0]][pos_key[1]] = s_num # 지도에 적용
            s_info[s_num][0] = pos_key # 좌표 정보 변경
            



direc = [(-1, 0), (1, 0), (0, 1), (0, -1)] # 위 아래 오른쪽 왼쪽
R, C, M = map(int, input().split())
graph = [[0] * C for _ in range(R)]
s_info = dict()
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[r - 1][c - 1] = i + 1
    s_info[i + 1] = [(r - 1, c - 1), s, d - 1, z] # 위치 / 속력 / 이동 방향 / 상어 크기

fish_king = 0
answer = 0
while fish_king < C:
    # 땅에 가장 가까운 상어 잡기
    for i in range(R):
        if graph[i][fish_king] != 0:
            s_num = graph[i][fish_king]
            answer += s_info[s_num][3]
            graph[i][fish_king] = 0
            s_info.pop(s_num)
            break
    
    #상어 이동
    shark_move()
    
    # 낚시왕 이동
    fish_king += 1
print(answer)