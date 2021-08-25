def laddering():
    for i in range(N):
        temp = i
        for j in range(H):
            if temp < N - 1 and ladder[j][temp]:
                temp += 1
            elif temp > 0 and ladder[j][temp - 1]:
                temp -= 1
        if temp != i:
            return False
    return True


def solve(count, row, limit):
    global answer

    if count == limit and laddering():
        answer = count
        return

    for i in range(row, H):
        for j in range(N - 1):
            if ladder[i][j]:
                continue
            if j - 1 >= 0 and ladder[i][j - 1]:
                continue
            if j + 1 < N - 1 and ladder[i][j + 1]:
                continue

            ladder[i][j] = True
            solve(count + 1, i, limit)
            ladder[i][j] = False


N, M, H = map(int, input().split()) # 열, 가로선 개수, 행


ladder = [[False] * (N - 1) for _ in range(H)]

for _ in range(M):
    x, y = tuple(map(int, input().split()))
    ladder[x - 1][y - 1] = True

answer = -1
searched = False

for l in range(4):
    solve(0, 0, l)
    if answer != -1:
        print(answer)
        searched = True
        break
if not searched:
    print(-1)