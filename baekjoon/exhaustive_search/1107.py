start = 100
n = int(input())
num_split = [int(''.join(num)) for num in list(str(n))]
m = int(input())

standard_answer = abs(n - start)
answer = standard_answer

if m in range(1, 10):
    excepts = [int(''.join(n)) for n in input().split(' ')]
    alive_num = [n for n in range(0, 10) if n not in excepts]

    for i in range(1000001):
        temp_list = set([int(''.join(n)) for n in list(str(i))])
        if temp_list.issubset(set(alive_num)):
            answer = min(answer, len(str(i)) + abs(n - i))
    print(answer)
elif m == 10:
    print(standard_answer)
else:
    print(min(standard_answer, len(str(n))))