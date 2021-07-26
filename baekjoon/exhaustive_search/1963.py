def prime(num):
    if num < 2:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def solve(num, nums, visited):
    visited[]

    for n in nums:



T = int(input())
for i in range(T):
    A, B = [int(''.join(n)) for n in input().split(' ')]
    answer = 0

    i = 0
    while True:
        if A == B:
            if prime(A):
                print(answer)
            else:
                print("Impossible")
            break

        if prime(A):
            i += 1

        strA = int(str(A)[i])
        if i == 0:
            nums = [n for n in range(9, 0, -1) if n != strA]
        else:
            nums = [n for n in range(9, -1, -1) if n != strA]

        for n in nums:
            A = str(A)
            A[i] = str(n)
            A = int(A)

            if prime(A):
                answer += 1
                i += 1
                break
            else:
                continue




