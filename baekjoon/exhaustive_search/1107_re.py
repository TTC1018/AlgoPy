N = int(input())
M = int(input())

answer = abs(N - 100)
if M in range(1, 10):
    alive_num = [n for n in range(0, 10) if n not in [int(''.join(num)) for num in input().split(' ')]]
    for i in range(1000000 + 1):
        temp_split = set([int(''.join(n)) for n in list(str(i))])
        if temp_split.issubset(set(alive_num)):
            answer = min(answer, len(str(i)) + abs(N - i))
    print(answer)
elif M == 10:
    print(answer)
else:
    print(min(answer, len(str(N))))