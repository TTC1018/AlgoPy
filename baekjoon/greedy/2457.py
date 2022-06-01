import sys

N = int(sys.stdin.readline().rstrip())
flower = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
flower.sort(key=lambda x: (x[0], x[1]))

answer = 0
fm, fd = 3, 1

i = 0
while i < N:
    tm, td = fm, fd # 새 꽃을 고를 기준점 (꽃의 개화 시작 시기가 이 변수들 이하 여야함)
    for j in range(i, N):
        fsm, fsd, fem, fed = flower[j]
        if fsm > tm or (fsm == tm and fsd > td): # 개화시작 기준점을 넘어서는 꽃일 때
            i = j # 다음 싸이클을 위해 인덱스 기록
            break
        if fem > fm or (fem == fm and fed > fd): # 더 오래 지속되는 꽃일 때
            fm, fd = flower[j][2:]

    if (tm, td) == (fm, fd): # 새로 갱신 안 됐다 = 더 이상 시기상 겹쳐지는 꽃이 없음
        break
    answer += 1
    if fm >= 12: # 이미 문제 조건 충족하면 더 탐색할 필요 없으므로 break
        break


if fm >= 12:
    print(answer)
else:
    print(0)