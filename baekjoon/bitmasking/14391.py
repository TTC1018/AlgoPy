import sys
input = sys.stdin.readline


def btk(pos, mask):
    global answer
    if pos == N * M:
        result = 0

        # 가로 종이 더하기
        for i in range(N):
            j = 0
            while j < M:
                tmp = str(P[i][j])
                if mask & (1 << (i * M + j)):
                    tmp_idx = j + 1
                    while tmp_idx < M and mask & (1 << (i * M + tmp_idx)):
                        tmp += str(P[i][tmp_idx])
                        tmp_idx += 1
                    result += int(tmp)
                    j = tmp_idx
                else:
                    j += 1

        # 세로 종이 더하기
        for j in range(M):
            i = 0
            while i < N:
                tmp = str(P[i][j])
                if not mask & (1 << (i * M + j)):
                    tmp_idx = i + 1
                    while tmp_idx < N and not mask & (1 << (tmp_idx * M + j)):
                        tmp += str(P[tmp_idx][j])
                        tmp_idx += 1
                    result += int(tmp)
                    i = tmp_idx
                else:
                    i += 1

        answer = max(answer, result)
        return


    nxt = pos + 1
    btk(nxt, mask | (1 << pos)) # 가로 표시
    btk(nxt, mask) # 세로 표시



N, M = map(int, input().split())
P = [list(map(int, list(input().rstrip()))) for _ in range(N)]
answer = 0
btk(0, 0)
print(answer)