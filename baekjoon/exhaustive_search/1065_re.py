def solve(num):
    pieces = list(map(int, num))
    length = len(pieces)

    if length <= 2:
        return True
    else:
        dif = abs(pieces[1] - pieces[0])
        for i in range(0, length - 1):
            temp = abs(pieces[i + 1] - pieces[i])
            if temp != dif:
                return False
        return True

N = input()

answer = 0
for i in range(1, int(N) + 1):
    if solve(str(i)):
        answer += 1

print(answer)