from itertools import permutations


def solution(expression):
    answer = 0
    
    sign = ['*', '-', '+']
    for order in permutations(sign):
        result = []
        f_op = expression.split(order[0]) # 마지막에 계산할 연산자 지우기
        for splt in f_op:
            s_op = splt.split(order[1]) # 두번째 연산자 지우기
            s_op = [str(eval(fmla)) for fmla in s_op] # 첫번째 연산자 계산
            result.append(order[1].join(s_op)) # 두번째 연산자 다시 붙이기
        result = [str(eval(fmla)) for fmla in result]
        
        tmp_answer = abs(eval(order[0].join(result))) # 마지막 연산자로 계산
        if answer < tmp_answer:
            answer = tmp_answer    
    
    return answer


solution("100-200*300-500+20")