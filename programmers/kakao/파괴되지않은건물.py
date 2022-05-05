def solution(board, skill):
    answer = 0
    ps = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for s in skill:
        type, r1, c1, r2, c2, degree = s
        if type == 1: # 공격
            ps[r1][c1] -= degree
            ps[r2 + 1][c2 + 1] -= degree
            ps[r2 + 1][c1] += degree
            ps[r1][c2 + 1] += degree
        elif type == 2: # 회복
            ps[r1][c1] += degree
            ps[r2 + 1][c2 + 1] += degree
            ps[r2 + 1][c1] -= degree
            ps[r1][c2 + 1] -= degree

    # 누적합 기록을 이용한 시간 복잡도 줄이기
    #     -3 -3 0               -3 0 3
    #     -3 -3 0                0 0 0
    #      0  0 0 의 공격을 하려면 3 0 -3 을 좌->우 위->아래 누적합 하면 됨
    # 이것을 하나의 누적합 2차원 배열에 모조리 기록해서 마지막에 원본과 합해서 비교
    r_len, c_len = len(board), len(board[0])
    for i in range(c_len + 1):
        for j in range(1, r_len + 1):
            ps[j][i] += ps[j - 1][i]
    for i in range(r_len + 1):
        for j in range(1, c_len + 1):
            ps[i][j] += ps[i][j - 1]

    for i in range(r_len):
        for j in range(c_len):
            if board[i][j] + ps[i][j] > 0:
                answer += 1

    return answer


print(solution(	[[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
                   [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))