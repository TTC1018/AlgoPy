import sys
input = sys.stdin.readline


def seperate(x, y, d1, d2):
    fixed = [[False] * (N + 1) for _ in range(N + 1)]
    fixed[x][y] = True
    for i in range(1, d1 + 1):
        fixed[x + i][y - i] = True
        fixed[x + d2 + i][y + d2 - i] = True
    for i in range(1, d2 + 1):
        fixed[x + i][y + i] = True
        fixed[x + d1 + i][y - d1 + i] = True

    # 1번 선거구
    sum_one = 0
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if fixed[r][c]:
                break
            sum_one += A[r][c]

    # 2번 선거구
    sum_two = 0
    for r in range(1, x + d2 + 1):
        for c in range(N, y, -1):
            if fixed[r][c]:
                break
            sum_two += A[r][c]

    # 3번 선거구
    sum_three = 0
    for r in range(x + d1, N + 1):
        for c in range(1, y - d1 + d2):
            if fixed[r][c]:
                break
            sum_three += A[r][c]

    # 4번 선거구
    sum_four = 0
    for r in range(x + d2 + 1, N + 1):
        for c in range(N, y - d1 + d2 - 1, -1):
            if fixed[r][c]:
                break
            sum_four += A[r][c]

    sum_five = total - (sum_one + sum_two + sum_three + sum_four)
    sums = [sum_one, sum_two, sum_three, sum_four, sum_five]
    max_val, min_val = max(sums), min(sums)
    return max_val - min_val


N = int(input())
A = [[0]] + [[0] + list(map(int, input().split())) for _ in range(N)]
total = 0
for a in A:
    total += sum(a)

answer = int(1e9)
for x in range(1, N + 1):
    for y in range(1, N + 1):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):
                if x + d1 + d2 <= N and y - d1 >= 1 and y + d2 <= N:
                    answer = min(answer, seperate(x, y, d1, d2))
print(answer)