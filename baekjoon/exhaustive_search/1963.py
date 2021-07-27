from collections import deque
import math
import copy

def prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solve(A, B):
    global answer
    q = deque([[list(str(A)), 0]])
    visited = {A}

    while True:
        num, answer = q.popleft()
        if int(''.join(num)) == B:
            print(answer)
            return
        else:
            for i in range(4):
                for j in range(10):
                    if num[i] == j:
                        continue
                    else:
                        temp = copy.deepcopy(num)
                        temp[i] = str(j)
                        temp = int(''.join(temp))
                        if temp not in visited and temp > 1000 and prime(temp):
                            visited.add(temp)
                            q.append([temp, answer + 1])


T = int(input())
for i in range(T):
    A, B = [int(''.join(n)) for n in input().split(' ')]
    answer = 0

    solve(A, B)
    if A != B:
        print("Impossible")





