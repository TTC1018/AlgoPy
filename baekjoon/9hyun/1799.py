import sys
input = sys.stdin.readline


in_range = lambda x, y: 0 <= x < N and 0 <= y < N
direc = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
def can_put(x, y):
    for d in direc:
        nx, ny = x + d[0], y + d[1]
        while in_range(nx, ny):
            if visited[nx][ny]: # 비숍있으면
                return False
            nx, ny = nx + d[0], ny + d[1]
    return True


def dfs(pos, type, count):
    x, y = pos
    total = x * N + y
    if N**2 - total + 1 + count <= answer[type]: # 남은 칸 다 채워도 답보다 적을 때
        return

    answer[type] = max(answer[type], count)
    j = y
    for i in range(x, N):
        while j < N:
            if not visited[i][j]:
                visited[i][j] = True
                if board[i][j] == 1 and can_put(i, j):
                    dfs((i, j), type, count + 1)
                visited[i][j] = False
            j += 2 # 같은 홀수/짝수칸만 탐색
        j = (type + 1) % 2 if i % 2 == 0 else type 
        # 홀수 행 = 흰칸은 인덱스1부터 검정칸은 인덱스0부터
        # 짝수 행 = 흰칸은 인덱스0부터 검정칸은 인덱스1부터
    

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
answer = [0, 0]

dfs((0, 0), 0, 0) # 흰칸
dfs((0, 1), 1, 0) # 검정칸
# 따로따로 탐색함으로써 시간복잡도를 반으로 줄일 수 있음
print(sum(answer))