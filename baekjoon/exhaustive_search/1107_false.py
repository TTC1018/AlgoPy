# 리모컨
# 각 자릿 수마다 가까운 값 ?? -> 최종적으로 가장 근접한 값이 나오지 않음

start = 100
n = int(input())
num_split = [int(''.join(num)) for num in list(str(n))]
standard_answer = abs(n - start)

m = int(input())
if m in range(1, 10) :
    excepts = [int(''.join(n)) for n in input().split(' ')]
    alive_num = [n for n in range(0, 10) if n not in excepts]

    temp_answer = []
    for i in range(0, len(num_split)):
        temp_list = [abs(n - num_split[i]) for n in alive_num]
        idx = temp_list.index(min(temp_list))
        temp_answer.append(str(alive_num[idx]))

    answer = ''.join(temp_answer)
    answer = len(answer) + abs(n - int(answer))
    print(min(answer, standard_answer))
elif m == 10:
    input()
    print(standard_answer)
else:
    print(min(len(num_split), standard_answer))