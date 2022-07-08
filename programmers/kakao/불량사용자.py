from itertools import permutations
import re


def solution(user_id, banned_id):
    answer = set()

    b_len = len(banned_id)
    for i in range(b_len):
        banned_id[i] = banned_id[i].replace('*', '.{1}')

    for cand in permutations(user_id, b_len):
        for i in range(b_len):
            if not re.fullmatch(banned_id[i], cand[i]):
                break
        else:
            answer.add(tuple(sorted(cand)))
    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))