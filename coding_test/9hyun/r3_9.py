def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2 + 1):
        t_a1, t_a2 = len(s), 0
        for j in range(0, len(s) - i, i):
            if s[j: j + i] == s[j + i: j + i + i]:
                t_a2 += i
            else:
                if t_a2 > 0:
                    t_a1 -= (t_a2 - len(str(t_a2 // i)))
                t_a2 = 0

            if j == len(s) - i - i and t_a2 > 0:
                t_a1 -= (t_a2 - len(str(t_a2 // i)))
        answer = min(answer, t_a1)

    return answer

print(solution(input()))