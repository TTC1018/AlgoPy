def solution(msg):
    answer = []

    d = {chr(alpha): alpha - 64 for alpha in range(ord('A'), ord('Z') + 1)}
    idx_num = 27
    m_len = len(msg)
    i = 0
    while i < m_len:
        for j in range(m_len - i, 0, -1):  # 긴 문자열부터 탐색
            s = msg[i: i + j]
            if s in d:
                if i + j >= m_len:
                    answer.append(d[s])
                else:
                    d[s + msg[i + j]] = idx_num
                    answer.append(d[s])
                    idx_num += 1
                i += len(s)
                break
    return answer


print(solution('KAKAO'))
