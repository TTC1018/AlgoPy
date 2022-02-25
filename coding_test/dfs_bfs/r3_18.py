def check_complete(strs):
    left = 0
    for s in strs:
        if s == '(':
            left += 1
        else:
            if left <= 0:
                return False
            left -= 1
    return True


def find_balance(strs):
    left = 0
    for i in range(len(strs)):
        if strs[i] == '(':
            left += 1
        else:
            left -= 1

        if left == 0:
            return i


def solution(p):
    answer = ''
    if p == '': # 1. 빈 문자열 반환
        return answer

    split = find_balance(p) # '균형잡힌 괄호 문자열' 지점 찾기
    u, v = p[:split + 1], p[split + 1:]

    if check_complete(u): # 3-1. u가 '올바른 괄호 문자열'이라면
        answer = u + solution(v) # v에 대해 1단계부터 다시 시행
    else: # 4. u가 '올바른 괄호 문자열'이 아니라면
        # 4-1. 빈 문자열에 첫번째 문자로 '(' 붙이고
        # 4-2. v에 대해 다시 시행
        # 4-3. ')'를 다시 붙임
        answer = '(' + solution(v) + ')'
        u = list(u[1:-1]) # 4-4. u의 첫번째와 마지막 문자 제거

        for i in range(len(u)): # 나머지 문자열의 괄호 방향을 뒤집어서
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u) # 뒤에 붙이기

    return answer