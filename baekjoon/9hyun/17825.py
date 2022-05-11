def init_field():
    global way, scores
    scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, # 0 ~ 10
              22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0, # 11 ~ 21
              13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35] # 22 ~ 32
    way = {}
    for i in range(21):
        lst = []
        for j in range(5):
            if i + j + 1 >= 21:
                lst.append(21)
                break
            else:
                lst.append(i + j + 1)
        way[i] = lst
    line_10 = [5, 22, 23, 24, 25, 31, 32, 20, 21] # 10 라인
    line_20 = [10, 26, 27, 25, 31, 32, 20, 21] # 20 라인
    line_30 = [15, 28, 29, 30, 25, 31, 32, 20, 21] # 30 라인

    for i in range(len(line_10)):
        way[line_10[i]] = line_10[i + 1:i + 6]
    for i in range(len(line_20)):
        way[line_20[i]] = line_20[i + 1:i + 6]
    for i in range(len(line_30)):
        way[line_30[i]] = line_30[i + 1:i + 6]


def dfs(count, score):

    if count == 10:
        return score

    dice = dices[count]
    max_score = score
    for i in range(4):
        if pieces[i] == 21: # 이미 도착
            continue
        if len(way[pieces[i]]) < dice:  # 다음 칸이 도착칸
            next_index = 21
        else:
            next_index = way[pieces[i]][dice - 1]
        if next_index in pieces and next_index != 21:
            continue
        cur_index = pieces[i]
        pieces[i] = next_index
        max_score = max(max_score, dfs(count + 1, score + scores[next_index]))
        pieces[i] = cur_index
    return max_score


dices = list(map(int, input().split()))

# 출발,도착 포함 33개 / 자식 index, 자신 점수
way = {}
pieces = [0, 0, 0, 0]
scores = []

init_field()
answer = dfs(0, 0)
print(answer)