from collections import defaultdict
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < N


def seperate(pos, m_sum, s_sum, cnt, flag):
    x, y = pos
    m_seper, s_seper = m_sum // 5, s_sum // cnt
    if m_seper > 0: # 질량 0 초과할 때 (0이면 소멸)
        if flag: # 0, 2, 4, 6
            for new_d in [0, 2, 4, 6]:
                fires.append([x, y, m_seper, s_seper, new_d])
        else: # 1, 3, 5, 7
            for new_d in [1, 3, 5, 7]:
                fires.append([x, y, m_seper, s_seper, new_d])


def move():
    new_loc = defaultdict(list)

    for fire in fires:
        f_r, f_c, f_m, f_s, f_d = fire

        nr, nc = f_r + f_s * direc[f_d][0], f_c + f_s * direc[f_d][1]
        if not in_range(nr, nc):
            nr, nc = nr % N, nc % N
        new_loc[(nr, nc)].append([f_m, f_s, f_d])

    fires.clear()
    for loc in new_loc:
        cnt = len(new_loc[loc])
        if cnt > 1: # 2개 이상일 때
            m_sum, s_sum = 0, 0
            odd_flag, even_flag = False, False

            for f in new_loc[loc]:
                f_m, f_s, f_d = f
                m_sum += f_m
                s_sum += f_s
                if f_d % 2 == 0:
                    even_flag = True
                else:
                    odd_flag = True

            if odd_flag and even_flag:
                seperate(loc, m_sum, s_sum, cnt, False)
            else:
                seperate(loc, m_sum, s_sum, cnt, True)
        else: # 1개 일때
            fires.append(list(loc) + new_loc[loc][0][:])


direc = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
N, M, K = map(int, input().split())
fires = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r, c = r - 1, c - 1
    fires.append([r, c, m, s, d])

for _ in range(K):
    move()

answer = 0
for fire in fires:
    answer += fire[2]
print(answer)