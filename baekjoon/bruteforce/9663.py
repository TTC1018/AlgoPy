def possible(now):
    for prev in range(now):
        if abs(Q[now] - Q[prev]) == abs(now - prev): # 대각선
            return False
    return True


def btk(now, mask):
    global answer

    if now == N:
        answer += 1
        return
    for y in range(N):
        if not (mask & (1 << y)):
            Q[now] = y
            if possible(now):
                btk(now + 1, mask | (1 << y))


N = int(input())
Q = [0] * N
answer = 0
btk(0, 0)
print(answer)