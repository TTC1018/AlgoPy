from collections import defaultdict


def solution(gems):
    INF = int(1e9)
    answer = [0, 0]
    
    gem = defaultdict(int)
    g_len = len(gems)
    cate_gem = len(set(gems))
    
    cand = []
    start, end = 0, 0
    while True:
        had = len(gem)
        if had == cate_gem: # 보석 다 갖고 있을 때
            if start == g_len:
                break
            cand.append((start, end)) # 후보에 저장
            gem[gems[start]] -= 1 # 지금 가리키는 보석 카운트 해제
            if gem[gems[start]] == 0:
                del gem[gems[start]]
            start += 1 # start 늘리기
        else: # 아직 보석 부족할 때
            if end == g_len:
                break
            gem[gems[end]] += 1 # 지금 가리키는 보석 카운트
            end += 1 # end 늘리기
    
    tmp_len = INF
    for start, end in cand:
        if end - start < tmp_len:
            tmp_len = end - start
            answer = start + 1, end
    
    return answer