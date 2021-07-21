N, K = [int(''.join(n)) for n in input().split(' ')]

def minus_one(N, sum):
    global answer

    if(N == K):
        return

    new_N = N-1

    answer += 1
    minus_one(new_N)
    plus_one(new_N)
    double_one(new_N)

def plus_one(N):
    global answer

    if (N == K):
        return

    new_N = N + 1

    answer += 1
    minus_one(new_N)
    plus_one(new_N)
    double_one(new_N)

def double_one(N):
    global answer

    if (N == K):
        return

    new_N = N * 2

    answer += 1
    minus_one(new_N)
    plus_one(new_N)
    double_one(new_N)

answer = 0
minus_one(N)
plus_one(N)
double_one(N)

print(answer)