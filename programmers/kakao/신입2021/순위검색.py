from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []

    info_dict = defaultdict(list)
    for i in info:
        data = i.split(' ')
        score = int(data[-1])
        data = data[:-1]

        for cnt in range(5):
            for c in combinations([0, 1, 2, 3], cnt): # info가 해당될 수 있는 모든 경우의 수를 확인하고 딕셔너리에 기록 ('-'이 있는 경우의 수에 포함될 수 있기 때문에)
                data_cpy = data[:]
                for idx in c:
                    data_cpy[idx] = '-'
                info_dict[''.join(data_cpy)].append(score)
    for key in info_dict:
        info_dict[key].sort() # 추후 이진탐색을 위해 오름차순 정렬해둠

    query = [tuple([new_q for new_q in q.replace('and', '').split(' ') if new_q != '']) for q in query]
    for q in query:
        target = ''.join(q[:-1])
        answer.append(len(info_dict[target]) - bisect_left(info_dict[target], int(q[-1])))

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))