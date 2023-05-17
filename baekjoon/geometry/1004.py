import sys
input = sys.stdin.readline


for _ in range(int(input())):
    sx, sy, dx, dy = map(int, input().split())
    n = int(input())
    P = [tuple(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for px, py, pr in P:
        s_dist = (sx - px)**2 + (sy - py)**2
        d_dist = (dx - px)**2 + (dy - py)**2
        p_dist = pr*pr

        if s_dist < p_dist and d_dist < p_dist: # 같은 영역 내에 존재
            continue
        elif s_dist < p_dist or d_dist < p_dist: # 둘 중에 하나만 존재하는 영역
            cnt += 1
    print(cnt)