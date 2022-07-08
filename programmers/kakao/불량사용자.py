from collections import defaultdict
import re


def solution(user_id, banned_id):

    d = defaultdict(set)
    for b in banned_id:
        regex = re.compile(b.replace('*', '.{1}'))
        for u in user_id:
            if regex.fullmatch(u):
                d[b].add(u)



    if not d:
        return 0

    answer = 1
    for key in d:
        answer *= len(d[key])

    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))