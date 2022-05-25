from collections import defaultdict


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    s1_len, s2_len = len(str1), len(str2)
    s1 = defaultdict(int)
    for i in range(s1_len - 1):
        target = str1[i:i+2]
        for j in range(2):
            if not target[j].isalpha():
                break
        else:
            s1[target] += 1
    s2 = defaultdict(int)
    for i in range(s2_len - 1):
        target = str2[i:i + 2]
        for j in range(2):
            if not target[j].isalpha():
                break
        else:
            s2[target] += 1

    checked = set()
    overlap, joined = 0, 0
    for k in s1:
        if k in s2 and k not in checked: # 교집합인 경우
            overlap += min(s1[k], s2[k])
            joined += max(s1[k], s2[k])
            checked.add(k)
        if k not in s2:
            joined += s1[k]
    for k in s2:
        if k not in s1:
            joined += s2[k]

    answer = 65536
    if joined:
        answer = int((overlap / joined) * 65536)
    return answer

print(solution('E=M*C^2', 'e=m*c^2'))