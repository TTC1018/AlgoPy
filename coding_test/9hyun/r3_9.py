def solution(s):
    answer = len(s) # 최대 길이로 초기화 (원본 문자열 길이)

    # 길이 1 ~ 원본길이 / 2 까지 축약할 수 있는지 확인
    # 원본길이 / 2 를 넘어서면 어차피 축약 불가능
    for i in range(1, len(s)//2 + 1):
        t_a1, t_a2 = len(s), i
        for j in range(0, len(s) - i, i):
            if s[j: j + i] == s[j + i: j + i + i]: # 반복되는 문자열인지 확인 (축약 가능한지)
                t_a2 += i
            else: # 반복되는 문자열이 아닐 때, 새 문자열이 등장했을 때
                if t_a2 > i: # 문자열이 2번이상 반복되었을 때
                    t_a1 -= (t_a2 - len(str(t_a2 // i)) - i) # (반복되는 문자열들의 총 길이 - 반복된 횟수를 나타내는 숫자의 길이 - 반복되는 문자열의 길이)를 차감
                t_a2 = i # 다시 초기화

            if j == len(s) - i - i and t_a2 > i: # 마지막 인덱스일 때 위 조건문을 통과하게 되는 경우를 고려해서 조건문 설정
                t_a1 -= (t_a2 - len(str(t_a2 // i)) - i)
        answer = min(answer, t_a1) # 최소값일 때 저장

    return answer


print(solution(input()))