import re
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    regex = input().rstrip()
    target = input().rstrip()

    a_cnt = 0
    answer = ''
    for alpha in range(ord('A'), ord('Z') + 1):
        temp = regex.replace('_', chr(alpha)) # 알파벳 대입해보기

        if re.fullmatch(temp, target):
            answer = chr(alpha)
            a_cnt += 1

    if a_cnt > 1:
        print('_')
    elif not answer:
        print('!')
    else:
        print(answer)