def solution(N, stages):
    f_rate = [[n, 0] for n in range(N + 1)] # 1 ... N 까지 각 숫자의 실패율 저장 리스트

    for i in range(1, N + 1):
        y = len([n for n in stages if n >= i]) # i-스테이지에 도달한 플레이어 수
        if y == 0:
            f_rate[i][1] = 0 # 0으로 나누는 경우를 방지
        else:
            f_rate[i][1] = (stages.count(i) / y) # 스테이지에 도달했으나 클리어 하지 않은 수 / 도달한 플레이어 수

    del f_rate[0] # 초기화 과정에서 생긴 i=0 데이터 삭제
    f_rate.sort(key=lambda x: (-x[1], x[0])) # 조건대로 정렬

    answer = [n[0] for n in f_rate] # 실패율 빼고 리스트 재구성
    return answer