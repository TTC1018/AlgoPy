def solution(n, weak, dist):

    dist.sort(reverse=True) # 내림차순으로 재정렬 (긴 길이부터 확인해야 사용되는 인원의 최솟값을 찾을 수 있음)
    w_len = len(weak)
    cand = [()] # 공집합을 넣어둬야 초기에 25라인을 지나치지 않음
    
    d_count = 0 # 사용된 인원 숫자
    for d in dist:
        d_count += 1
        
        coverage = [] # 커버 가능한 영역
        for idx, w in enumerate(weak):
            head = w
            tail = weak[idx:] + [n+i for i in weak[:idx]] 
            # head보다 아래 인덱스는 한바퀴 돌아서 도착하는 것과 같기 때문에
            # n을 더해서 반시계로 회전했을 때의 거리로 바꿔줌
            
            temp_cover = [t % n for t in tail if t - head <= d] 
            # 거리 d로 커버 가능한 포인트
            # 후보에 추가할 때는 더해준 n을 제거하기 위해 % n 연산을 처리
            coverage.append(set(temp_cover))
    
        temp_cand = set()
        for c in coverage:
            for origin_c in cand:
                new = c | set(origin_c) # 합집합
                if len(new) == w_len: # 취약지점 모두 커버 된 경우
                    return d_count
                temp_cand.add(tuple(new)) # set에 set을 저장하는 것은 불가하므로 일단은 튜플로 변환하여 저장
        cand = temp_cand

    
    return -1