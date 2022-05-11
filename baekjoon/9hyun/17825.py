import sys
input = sys.stdin.readline


def dfs(count, sum_val):
    global answer

    if count == 10:
        answer = max(answer, sum_val)
        return

    dice = dices[count]  # 현재 주사위로 갈 칸
    for i in range(4):
        line, pos = piece[i] # 현재 라인, 라인 내 위치
        end_point = len(board[line]) - 1

        if pos == end_point: # 이미 도착한 말
            continue
        elif pos + dice >= end_point: # 더 가면 도착 지점인 경우
            piece[i][1] = end_point
            dfs(count + 1, sum_val)
            piece[i][1] = pos
        else: # 도착 지점 아닌 경우
            pos = pos + dice
            score = board[line][pos]  # 도착할 칸 점수

            if line == 0:
                if pos in [5, 10, 15]:
                    if [score, 0] in piece:
                        continue
                    else:
                        piece[i] = [score, 0]
                        dfs(count + 1, sum_val + score)
                        piece[i] = [line, pos - dice]
                elif pos == 20:
                    if [10, 7] in piece or [20, 6] in piece or [30, 7]:
                        continue
                    else:
                        piece[i][1] = pos  # 라인 내 위치 갱신
                        dfs(count + 1, sum_val + score)
                        piece[i][1] = pos - dice
                else:
                    if [line, pos] in piece:
                        continue  # 이미 다른 말이 대기중일 때

                    piece[i][1] = pos  # 라인 내 위치 갱신
                    dfs(count + 1, sum_val + score)
                    piece[i][1] = pos - dice
            else:
                if line == 10:
                    if [20, pos - 1] in piece or [30, pos] in piece:
                        continue
                    elif pos == end_point - 1:
                        if [0, 20] in piece:
                            continue
                elif line == 20:
                    if [10, pos + 1] in piece or [30, pos + 1] in piece:
                        continue
                    elif pos == end_point - 1:
                        if [0, 20] in piece:
                            continue
                elif line == 30:
                    if [10, pos] in piece or [20, pos - 1] in piece:
                        continue
                    elif pos == end_point - 1:
                        if [0, 20] in piece:
                            continue

                if [line, pos] in piece:
                    continue  # 이미 다른 말이 대기중일 때

                piece[i][1] = pos # 라인 내 위치 갱신
                dfs(count + 1, sum_val + score)
                piece[i][1] = pos - dice



dices = list(map(int, input().split()))
board = {0: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, -1],
         10: [10, 13, 16, 19, 25, 30, 35, 40, -1],
         20: [20, 22, 24, 25, 30, 35, 40, -1],
         30: [30, 28, 27, 26, 25, 30, 35, 40, -1]}


piece = [[0, 0], [0, 0], [0, 0], [0, 0]] # 어떤 라인의 몇번째 칸에 있는지

answer = 0
dfs(0, 0)
print(answer)