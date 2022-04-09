from collections import defaultdict

# 시간을 분으로 변경
def time_to_minute(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m



def solution(fees, records):
    answer = dict()
    
    car = defaultdict(list)    
    s_time, s_fee, p_time, p_fee = fees
    for r in records:
        now, c_num, state = r.split(' ')
        if len(car[c_num]) == 0: # 아직 초기화 안 됐을 때
            car[c_num] = [now, 0, state]
        else: # 이전 기록 있을 때
            if state == 'OUT':
                prev, total, p_state = car[c_num] # 이전 기록 불러오기
                total += (time_to_minute(now) - time_to_minute(prev)) # 이전 기록과의 차이 계산
                car[c_num] = [now, total, state] # 새 값 적용
            else: # IN일 때
                car[c_num] = [now, car[c_num][1], state] # 새 값으로 갱신

    # 'IN' 상태에서 끝난 자동차들 시간 갱신
    for c in car:
        now, total, state = car[c]
        if state == 'IN':
            car[c][1] += (time_to_minute('23:59') - time_to_minute(now))

    # 기록된 값들 요금 계산
    for c in car:
        now, total, state = car[c]
        if total <= s_time: # 기본 시간 이하일 때
            answer[c] = s_fee
        else: # 기본 시간 초과했을 때
            temp_answer = s_fee # 기본 요금에서 시작
            total -= s_time
            
            rest, mod = divmod(total, p_time)
            if mod > 0: # 안 나눠 떨어질 때
                temp_answer += ((rest + 1) * p_fee)
            else: # 딱 나눠 떨어질 때
                temp_answer += (rest * p_fee)
            answer[c] = temp_answer
    
    answer = sorted(answer.items())
    
    result = []
    for a in answer:
        result.append(a[1])
    return result


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))