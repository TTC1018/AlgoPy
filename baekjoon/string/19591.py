import sys
input = sys.stdin.readline


def left_search():
    global s_len, stack
    left, right = '', ''
    for i in range(s_len):
        if S[i].isnumeric():
            if not stack:
                left += S[i]
            else:
                right += S[i]
        else:
            if not stack and left:
                stack.append(S[i])
            elif not left:
                left += S[i]
            else:
                return left, stack.pop(), right, False
    else:
        if stack:
            return left, stack.pop(), right, True
        else:
            return left, '', '', True


def right_search():
    global s_len, stack
    left, right = '', ''
    for i in range(s_len - 1, -1, -1):
        if S[i].isnumeric():
            if not stack:
                right += S[i]
            else:
                left += S[i]
        else:
            if not stack:
                stack.append(S[i])
            else:
                return left[::-1], stack.pop(), right[::-1]


S = input().rstrip()
stack = []
pd, pm = ['*', '/'], ['+', '-']
while True:
    s_len = len(S)
    
    ll, ls, lr, e_flag = left_search()
    if e_flag:
        if not lr:
            print(int(ll))
        else:
            ll, lr = str(int(ll)), str(int(lr))
            print(int(eval(ll + ls + lr)))
        break
    
    rl, rs, rr = right_search()
    
    if ls in pd and rs in pm:
        modi_len = len(ll + ls + lr)
        ll, lr = str(int(ll)), str(int(lr))
        result = int(eval(ll + ls + lr))
        S = str(result) + S[modi_len:]
    elif ls in pm and rs in pd:
        modi_len = len(rl + rs + rr)
        rl, rr = str(int(rl)), str(int(rr))
        result = int(eval(rl + rs + rr))
        S = S[:-modi_len] + str(result)
    else:
        l_len, r_len = len(ll + ls + lr), len(rl + rs + rr)
        ll, lr = str(int(ll)), str(int(lr))
        l_res = int(eval(ll + ls + lr))
        rl, rr = str(int(rl)), str(int(rr))
        r_res = int(eval(rl + rs + rr))
        
        if l_res < r_res:
            S = S[:-r_len] + str(r_res)
        else:
            S = str(l_res) + S[l_len:]