from itertools import permutations


def solution(numbers):

    coms = list(permutations(numbers, len(numbers)))
    print(coms)
    for i, c in enumerate(coms):
        coms[i] = int(''.join(list(map(str, c))))

    coms.sort()
    print(coms)
    answer = str(coms[-1])

    return answer

solution([6, 10, 2])