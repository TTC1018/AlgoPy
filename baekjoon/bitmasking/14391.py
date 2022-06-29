def btk(pos, mask):
    global answer
    if pos == N * M:
        result = 0

        visited = [False] * (1 << (N * M))
        visited[0] = True

        for idx in range(N * M):
            if not visited[idx]:
                visited[idx] = True
                r, c = divmod(idx, M)
                tmp = str(P[r][c])
                if mask & (1 << idx): # 가로
                    tmp_idx = idx + 1
                    c += 1
                    while c < M and mask & tmp_idx and not visited[tmp_idx]:
                        visited[tmp_idx] = True
                        tmp += str(P[r][c])
                        c += 1
                        tmp_idx += 1
                    result += int(tmp)
                else:
                    tmp_idx = idx + M
                    r += 1
                    while r < N and mask & tmp_idx and not visited[tmp_idx]:
                        visited[tmp_idx] = True
                        tmp += str(P[r][c])
                        r += 1
                        tmp_idx += M
                result += int(tmp)

        print(bin(mask), result)
        answer = max(answer, result)
        return


    nxt = pos + 1
    if pos >= M:
        if not mask & (1 << (pos - M)): # 이전 줄이 가로 아님
            btk(nxt, mask | (1 << pos))
        btk(nxt, mask)
    else:
        btk(nxt, mask | (1 << pos))
        btk(nxt, mask)



N, M = map(int, input().split())
P = [list(map(int, list(input()))) for _ in range(N)]
answer = 0
btk(0, 0)
print(answer)