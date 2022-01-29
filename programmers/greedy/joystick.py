def solution(name):
    # 상하 변경 횟수부터 합산
    answer1 = 0
    for n in name:
        answer1 += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)

    # 좌우 변경 횟수 계산
    # 좌 -> 우로 그대로 간다 쳤을 때 어디까지 가야할지를 확인
    end = len(name) - 1
    for i in range(len(name) - 1, -1, -1):
        if name[i] != 'A':
            end = i
            break
    answer2 = end

    # 좌 -> 우로 가다가 돌아가는 경우
    # A를 만날 때마다 돌아 가는 거리를 계산하기
    i = 0
    while i < len(name):
        if name[i] == 'A':
            a_end = i
            for j in range(i + 1, len(name)):
                if name[j] == 'A':
                    a_end = j
                else:
                    break
            if i > 0:
                answer2 = min(answer2, (i - 1) + (i - 1) + (len(name) - 1 - a_end))
            else:
                answer2 = min(answer2, len(name) - 1 - a_end)
            i += (a_end - i + 1)
        else:
            i += 1

    print(answer1, answer2)
    answer = answer1 + answer2
    return answer