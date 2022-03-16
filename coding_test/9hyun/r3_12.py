def isRight(answer):
    flag = True
    for ans in answer:
        x, y, a = ans
        if a == 0:  # 올바른 기둥인지 확인
            # 바닥의 기둥인지, 보의 위에 있는지, 다른 기둥 위에 있는지
            if not (y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer):
                flag = False
                break
        else:  # 올바른 보인지 확인
            # 적어도 한쪽이 기둥의 위에 있는지, 양쪽이 다른 보와 연결되어 있는지
            if not ([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)):
                flag = False
                break
    return flag


def solution(n, build_frame):
    answer = []
    # x, y, a, b
    # a => 구조물 종류 (0: 기둥, 1: 보)
    # b => 설치/삭제 명령어 (0: 삭제, 1: 설치)
    # 기둥은 x, y 위로, 보는 x, y 우측으로 설치/삭제
    # 조건 불충족하는 명령은 무시됨

    for build in build_frame:
        x, y, a, b = build
        if b == 0:  # 삭제
            answer.remove([x, y, a])
            if not isRight(answer):
                answer.append([x, y, a])
        else:  # 설치
            answer.append([x, y, a])
            if not isRight(answer):
                answer.remove([x, y, a])

    answer.sort()
    return answer