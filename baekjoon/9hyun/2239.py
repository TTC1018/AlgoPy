import sys
def back_tracking(count):
    if count == len(zero):
        for r in sudoku:
            print(*r, sep="")
        sys.exit()

    x, y = zero[count]
    bx, by = x // 3, y // 3
    cand_copy = cand[:]

    for i in range(bx * 3, (bx + 1) * 3):
        for j in range(by * 3, (by + 1) * 3):
            if sudoku[i][j] in cand_copy:
                cand_copy.remove(sudoku[i][j])
    for i in range(9):
        if sudoku[x][i] in cand_copy:
            cand_copy.remove(sudoku[x][i])
        if sudoku[i][y] in cand_copy:
            cand_copy.remove(sudoku[i][y])

    for c in cand_copy:
        sudoku[x][y] = c
        back_tracking(count + 1)
    sudoku[x][y] = 0


sudoku = [list(map(int, list(input()))) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0] # 사전 순 답으로 정해지려면 필수
cand = [i for i in range(1, 9 + 1)]
back_tracking(0)