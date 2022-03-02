# words = 가사의 모든 단어들 (2개 이상)
# queries = 찾고자 하는 키워드 (2개 이상)
def solution(words, queries):
    answer = []
    w_size = len(words)

    words.sort(key=lambda  x:len(x))
    for q in queries:
        q_len = len(q)
        l_qm, r_qm = 0, q_len - 1
        # 좌우 '?' 얼마나 있는지 확인
        for i in range(q_len):
            if q[i] != '?':
                break
            l_qm += 1
        for i in range(q_len, -1, -1):
            if q[i] != '?':
                break
            r_qm -= 1

        count = 0
        start, end = 0, w_size - 1
        mid = (start + end) // 2
        while start <= end:
            t_len = len(words[mid])
            if t_len > q_len:
                end = mid - 1
                continue
            elif t_len < q_len:
                start = mid + 1
                continue
            else:
                for i in range(len(words[mid])):
                    if w ==


        answer.append(count)


    return answer