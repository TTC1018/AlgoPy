def solve(y, x):
    global answer

    if y == N: # 목표까지 도달했으면 +1
        answer += 1
        return

    for i in range(N): # 다음 행에 속한 위치 전체 탐색
        flag = False
        for j in range(y + 1): # 탐색 대상의 열 검사
            if m[j][i]:
                flag = True
                print(j, i, 'first breaked')
                break

        if not flag:
            for j in range(-(N-1), N):
                ny, nx = y + j, x + j
                if 0 <= ny < N and 0 <= nx < N:
                    if m[ny][nx]:
                        flag = True
                        print(j, i, 'second breaked')
                        break

            if not flag:
                for j in range(-(N - 1), N):
                    ny, nx = y - j, x + j
                    if 0 <= ny < N and 0 <= nx < N:
                        if m[ny][nx]:
                            flag = True
                            print(j, i, 'third breaked')
                            break

                if not flag:
                    print(y + 1, i)
                    m[y + 1][i] = True
                    solve(y + 1, i)
                    m[y + 1][i] = False


N = int(input())
answer = 0

m = [[False] * N for _ in range(N)]
for i in range(N):
    m[0][i] = True
    solve(0, i)
    m[0][i] = False

print(answer)