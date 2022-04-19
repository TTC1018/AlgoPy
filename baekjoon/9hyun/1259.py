while True:
    target = input()
    if target == '0':
        break

    t_len = len(target)
    pivot = t_len // 2

    if t_len % 2 == 0:
        if target[:pivot] == target[pivot:][::-1]:
            print('yes')
        else:
            print('no')
    else:
        if target[:pivot] == target[pivot + 1:][::-1]:
            print('yes')
        else:
            print('no')