from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < M and 0 <= y < N
# 명령 1: GO (3칸까지 이동)
# 명령 2: TURN (좌 또는 우회전)
def bfs():
    q = deque()
    q.append((rx, ry, rd, 0))
    visited[rx][ry][rd] = True
    while q:
        x, y, d, cnt = q.popleft()
        if (x, y, d) == (lx, ly, ld):
            return cnt
    
        nx, ny = x, y
        for _ in range(3):
            nx, ny = nx + direc[d][0], ny + direc[d][1]
            if in_range(nx, ny) and not graph[nx][ny]:# 갈 수 있을 때
                if not visited[nx][ny][d]:
                    visited[nx][ny][d] = True
                    q.append((nx, ny, d, cnt + 1))
            else:
                break
            
        # 좌우 회전
        for new_turn in turn_dict[d]:
            if not visited[x][y][new_turn]:
                visited[x][y][new_turn] = True
                q.append((x, y, new_turn, cnt + 1))
        
        # 반대 회전
        opposite = opp_dict[d]
        if not visited[x][y][opposite]:
            visited[x][y][opposite] = True
            q.append((x, y, opposite, cnt + 2))


direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
turn_dict = {0:(2, 3), 1:(3, 2), 2:(0, 1), 3:(1, 0)}
opp_dict = {0:1, 1:0, 2:3, 3:2}
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
rx, ry, rd = map(int, input().split())
rx, ry, rd = rx - 1, ry - 1, rd - 1
lx, ly, ld = map(int, input().split())
lx, ly, ld = lx - 1, ly - 1, ld - 1

visited = [[[False for _ in range(4)] for _ in range(N)] for _ in range(M)]
answer = bfs()
print(answer)