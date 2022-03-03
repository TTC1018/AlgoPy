from bisect import bisect_left, bisect_right


def word_count(words, l_standard, r_standard):
    left = bisect_left(words, l_standard)
    right = bisect_right(words, r_standard)
    return right - left


# words = 가사의 모든 단어들 (2개 이상)
# queries = 찾고자 하는 키워드 (2개 이상)
def solution(words, queries):
    answer = []

    max_len = len(sorted(queries, key=lambda x:len(x))[-1]) # 제일 긴 쿼리 길이 확인

    word_arr = [[w for w in words if len(w) == i] for i in range(max_len + 1)]
    word_arr_rev = [[w[::-1] for w in words if len(w) == i] for i in range(max_len + 1)] # bisect를 이용할 것이기 때문에, ?가 앞쪽에 있는 쿼리들은 뒤집은 뒤 기존 사용법을 적용

    for i in range(max_len + 1):
        word_arr[i].sort()
        word_arr_rev[i].sort()

    for q in queries:
        q_len = len(q)

        if q[0] == '?':
            answer.append(word_count(word_arr_rev[q_len], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z')))
        else:
            answer.append(word_count(word_arr[q_len], q.replace('?', 'a'), q.replace('?', 'z')))

    return answer