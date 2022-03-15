def solution(n, build_frame):
    answer = [[]]

    # x, y, a, b
    # a => 구조물 종류 (0: 기둥, 1: 보)
    # b => 설치/삭제 명령어 (0: 삭제, 1: 설치)
    # 기둥은 x, y 위로, 보는 x, y 우측으로 설치/삭제
    # 조건 불충족하는 명령은 무시됨

    pillar = [[False] * n for _ in range(n)]
    top = [[False] * n for _ in range(n)]

    for build in build_frame:
        x, y, a, b = build
        if a == 0: # 기둥
            if b == 0: # 삭제
                pass
            else: # 설치
                if y == 0 or top[y][x]:
                    pillar[y][x] = True
        else: # 보
            if b == 0: # 삭제
                pass
            else: # 설치
                if pillar[y - 1][x] or pillar[y - 1][x - 1] or (top[y][x - 1] and top[y][x + 1]):
                    top[y][x] = True
                pass


    return answer