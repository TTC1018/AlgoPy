from copy import deepcopy

def dfs(lion, count, limit, apeach):
    global answer, max_diff
    if count == limit:
        temp_diff = compare_to_apeach(apeach, lion)
        if temp_diff > 0:
            if max_diff <= temp_diff:
                answer.append(deepcopy(lion))
                max_diff = temp_diff
        return
    elif count > limit:
        return
        
    for i in range(11):
        if i != 10:
            if apeach[i] >= lion[i]:
                temp_diff = (apeach[i] - lion[i] + 1)
                lion[i] += temp_diff
                dfs(lion, count + temp_diff, limit, apeach)
                lion[i] -= temp_diff
        else:
            lion[i] += (limit - count)
            dfs(lion, limit, limit, apeach)
            lion[i] -= (limit - count)


def compare_to_apeach(apeach, lion):
    a_score, l_score = 0, 0
    for i in range(11):
        if not (apeach[i] == 0 and lion[i] == 0):
            if apeach[i] < lion[i]:
                l_score += (10 - i)
            else:
                a_score += (10 - i)
    return l_score - a_score


def calc_arrows(arrows):
    result = 0
    for i in range(11):
        result += ((10 - i) * arrows[i])
    return result

# k점에 더 많이 맞춘 사람이 k점 가져감 (딱 k점만)
# 같은 발 맞췄으면 어피치가 가져감 -> 더 맞춰야됨
# 최종 점수가 더 높으면 우승 (같으면 어피치)
# 어피치가 쏜 화살 n개, 맞춘 곳 info (10 ~ 0)
answer = []
max_diff = 0
def solution(n, info):
    global answer, max_diff
    lion = [0] * 11
    dfs(lion, 0, n, info)
    if len(answer) == 0:
        return [-1]
    else:
        final = []
        for a in answer:
            if compare_to_apeach(info, a) == max_diff:
                final.append(a)
        final.sort(key = lambda x:(-x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))
        return final[0]


print(solution(	10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))