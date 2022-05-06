def str_to_num(str, idx):
    f_str = str[idx]
    if f_str == 'z':
        return '0', idx + 4
    elif f_str == 'o':
        return '1', idx + 3
    elif f_str == 't':
        nxt_str = str[idx + 1]
        if nxt_str == 'w':
            return '2', idx + 3
        else:
            return '3', idx + 5
    elif f_str == 'f':
        nxt_str = str[idx + 1]
        if nxt_str == 'o':
            return '4', idx + 4
        else:
            return '5', idx + 4
    elif f_str == 's':
        nxt_str = str[idx + 1]
        if nxt_str == 'i':
            return '6', idx + 3
        else:
            return '7', idx + 5
    elif f_str == 'e':
        return '8', idx + 5
    elif f_str == 'n':
        return '9', idx + 4



def solution(s):
    s_idx = 0
    s_len = len(s)

    converted = ''
    while s_idx < s_len:
        now_str = s[s_idx]
        if ord(now_str) >= 97: # 알파벳일 때
                now_converted, nxt_idx = str_to_num(s, s_idx)
                converted += now_converted
                s_idx = nxt_idx
        else:
            converted += now_str
            s_idx += 1

    return int(converted)


print(solution('one4seveneight'))