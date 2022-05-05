from collections import deque

in_range = lambda x, y: 0 <= x < 5 and 0 <= y < 5
direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def solution(places):
    answer = []
    # P = 앉은 자리 , O = 빈 테이블, X = 벽
    for i in range(5):  # 대기실들
        sit = deque()
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    sit.append(((j, k), (j, k), 0))

        stop_flag = False
        while sit and not stop_flag:
            org, pos, cnt = sit.popleft()
            x, y = pos
            for d in direc:
                nx, ny = x + d[0], y + d[1]
                if in_range(nx, ny):
                    if places[i][nx][ny] == 'P'and (nx, ny) != org:
                        answer.append(0)
                        stop_flag = True
                        break
                    elif places[i][nx][ny] == 'O':
                        if cnt == 0:
                            sit.append((org, (nx, ny), 1))

        if len(answer) < (i + 1):
            answer.append(1)

    return answer