from bisect import bisect_left, bisect_right


def l_q_search(q):
    l_qm = 0
    for i in range(len(q)):
        if q[i] != '?':
            break
        l_qm += 1
    return l_qm


def r_q_search(q):
    r_qm = len(q) - 1
    for i in range(len(q) - 1, -1, -1):
        if q[i] != '?':
            break
        r_qm -= 1
    return r_qm

# words = 가사의 모든 단어들 (2개 이상)
# queries = 찾고자 하는 키워드 (2개 이상)
def solution(words, queries):
    answer = []
    word_arr = [[] for _ in range(10001)]
    word_arr_rev = [[] for _ in range(10001)]

    for w in words:
        word_arr[len(w)].append(w)
        word_arr_rev[len(w)].append(w[::-1])

    w_size = len(words)

    words.sort(key=lambda x: (len(x), x))
    for q in queries:
        q_len = len(q)
        l_qm, r_qm = l_q_search(q), r_q_search(q)

        temp_answer = set()
        start, end = 0, w_size - 1
        while start <= end:
            mid = (start + end) // 2
            t_len = len(words[mid])
            if t_len > q_len:  # 대상 길이가 쿼리보다 긴 경우
                end = mid - 1
            elif t_len < q_len:  # 대상 길이가 쿼리보다 짧은 경우
                start = mid + 1
            else:
                if words[mid][l_qm:r_qm + 1] == q[l_qm:r_qm + 1]:
                    temp_answer.add(words[mid])
                    start = mid + 1
                else:
                    end = mid - 1

        start, end = 0, w_size - 1
        while start <= end:
            mid = (start + end) // 2
            t_len = len(words[mid])
            if t_len > q_len:  # 대상 길이가 쿼리보다 긴 경우
                end = mid - 1
            elif t_len < q_len:  # 대상 길이가 쿼리보다 짧은 경우
                start = mid + 1
            else:
                if words[mid][l_qm:r_qm + 1] == q[l_qm:r_qm + 1]:
                    temp_answer.add(words[mid])
                    end = mid - 1
                else:
                    start = mid + 1

        start, end = 0, w_size - 1
        while start <= end:
            mid = (start + end) // 2
            t_len = len(words[mid])
            if t_len > q_len:  # 대상 길이가 쿼리보다 긴 경우
                end = mid - 1
            elif t_len < q_len:  # 대상 길이가 쿼리보다 짧은 경우
                start = mid + 1
            else:
                if words[mid][l_qm:r_qm + 1] == q[l_qm:r_qm + 1]:
                    temp_answer.add(words[mid])
                end = mid - 1

        start, end = 0, w_size - 1
        while start <= end:
            mid = (start + end) // 2
            t_len = len(words[mid])
            if t_len > q_len:  # 대상 길이가 쿼리보다 긴 경우
                end = mid - 1
            elif t_len < q_len:  # 대상 길이가 쿼리보다 짧은 경우
                start = mid + 1
            else:
                if words[mid][l_qm:r_qm + 1] == q[l_qm:r_qm + 1]:
                    temp_answer.add(words[mid])
                start = mid + 1

        answer.append(len(temp_answer))

    return answer


result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
                  ["fro??", "????o", "fr???", "fro???", "pro?"])
print(result)
