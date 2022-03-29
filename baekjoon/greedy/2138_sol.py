def reverse(strs):
    result = ''
    for s in strs:
        if s == '0':
            result += '1'
        else:
            result += '0'
    return result


N = int(input())

now = input() # 첫번째 스위치 OFF
now2 = reverse(now[:2]) + now[2:] # 첫번째 스위치 ON
target = input()

if now[0] == target[0]:
    
    pass
else:
    pass