def check(x):
    for i in range(x):
        if m[x] == m[i] or abs(m[x] - m[i]) == x - i:
            return False
    return True


def solve(x):
    global answer

    if x == N: # 목표까지 도달했으면 +1
        answer += 1
    else:
        for i in range(N):
            m[x] = i
            if check(x):
                solve(x + 1)


N = int(input())
answer = 0
m = [0] * N
solve(0)
print(answer)