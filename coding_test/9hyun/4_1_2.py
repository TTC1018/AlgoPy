N = int(input())
H, M, S = 0, 0, 0

answer = 0
while H < N + 1:
    if '3' in ''.join(map(str, [H, M, S])):
        answer += 1

    S = S + 1

    if S == 60:
        S = 0
        M += 1

    if M == 60:
        M = 0
        H += 1

print(answer)