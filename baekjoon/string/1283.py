import sys
input = sys.stdin.readline

N = int(input())
O = [input().rstrip() for _ in range(N)]
d = dict()

answer = []
for option in O:
    pieces = option.split()

    # 단어 첫 글자 탐색
    for i in range(len(pieces)):
        if not d.get(pieces[i][0].lower()):
            d[pieces[i][0].lower()] = True
            pieces[i] = f'[{pieces[i][0]}]{pieces[i][1:]}'
            answer.append(' '.join(pieces))
            break
    else:  # 선택할 첫 글자 없음
        for j in range(len(option)):
            if option[j].isalpha() and not d.get(option[j].lower()):
                d[option[j].lower()] = True
                answer.append(f'{option[:j]}[{option[j]}]{option[j + 1:]}')
                break
        else:
            answer.append(option)
print('\n'.join(answer), end='')


