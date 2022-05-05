from collections import deque
from copy import deepcopy


def compare_to_apeach(apeach, lion):
    a_score, l_score = 0, 0
    for i in range(10):
        if apeach[i] < lion[i]:
            l_score += (10 - i)
        elif apeach[i] >= lion[i] and not (apeach[i] == 0 and lion[i] == 0):
            a_score += (10 - i)
    return l_score - a_score


def calc_arrows(arrows):
    result = 0
    for i in range(10):
        result += ((10 - i) * arrows[i])
    return result

# k점에 더 많이 맞춘 사람이 k점 가져감 (딱 k점만)
# 같은 발 맞췄으면 어피치가 가져감 -> 더 맞춰야됨
# 최종 점수가 더 높으면 우승 (같으면 어피치)
# 어피치가 쏜 화살 n개, 맞춘 곳 info (10 ~ 0)
def solution(n, info):
    lion = [0] * 11
    answer = [0] * 11
    max_diff = 0
    
    q = deque()
    q.append([lion, 0])
    while q:
        l, count = q.popleft()
        if count == n:
            temp_diff = compare_to_apeach(info, l)
            if temp_diff > 0:
                if max_diff < temp_diff:
                    answer = deepcopy(l)
                    max_diff = temp_diff
            continue
        elif count > n:
            continue
        
        
        for i in range(10):
            if info[i] >= l[i]:
                temp_l = deepcopy(l)
                diff = info[i] - l[i] + 1
                temp_l[i] += diff
                q.append([temp_l, count + diff])
    
    if calc_arrows(answer) == 0:
        return [-1]
    else:
        return answer


print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))