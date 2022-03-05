def rotation(oper):
    if toward == 'right':
        return 'down' if oper == 'D' else 'up'
    elif toward == 'left':
        return 'up' if oper == 'D' else 'down'
    elif toward == 'up':
        return 'right' if oper == 'D' else 'left'
    elif toward == 'down':
        return 'left' if oper == 'D' else 'right'


N = int(input())
K = int(input())
apple = [[False] * N for _ in range(N)]
for _ in range(K):
    R, C = map(int, input().split())
    apple[R - 1][C - 1] = True

direction = dict()
direction['right'] = (0, 1)
direction['left'] = (0, -1)
direction['up'] = (-1, 0)
direction['down'] = (1, 0)

tail, head, toward = (0, 0), (0, 0), 'right'
graph = [[False] * N for _ in range(N)]
graph[0][0] = True
pass_locs = []
# 벽 or 자기 몸에 부딪히면 게임 종료
second, flag = 0, False
L = int(input())
for _ in range(L):
    X, C = input().split()
    X = int(X)

    for i in range(X):
        second += 1
        hx, hy = head
        nhx, nhy = hx + direction[toward][0], hy + direction[toward][1]
        if 0 <= nhx < N and 0 <= nhy < N: # 벽에 부딪힌 게 아닐 때
            # 몸에 부딪혔는 지 확인
            if graph[nhx][nhy]:
                flag = True
                break
            else:
                head = (nhx, nhy)  # 머리는 새 좌표로
                pass_locs.append((nhx, nhy))
                if apple[nhx][nhy]:  # 사과 있을 때
                    apple[nhx][nhy] = False  # 사과 제거
                else:  # 사과 없을 때
                    tx, ty = tail
                    graph[tx][ty] = False
                    tail = (nhx, nhy)  # 꼬리도 이동
                    while pass_locs:
                        lx, ly = pass_locs.pop()
                        graph[lx][ly] = False
                graph[nhx][nhy] = True
        else: # 벽에 부딪혔을 때
            flag = True
            break
    toward = rotation(C)
    if flag:
        break
print(second)