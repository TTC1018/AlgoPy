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






def solution(p):
    answer = ''




    return answer