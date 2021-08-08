from itertools import combinations


while True:
    ip = input()
    if ip == '0':
        break

    nums = list(map(int, ip.split(' ')))
    k, S = nums[0], nums[1:]

    answer = combinations(S, 6)
    for a in answer:
        print(*a)
    print()