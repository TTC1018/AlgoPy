def solve(i, j):
    if sdk[i].count(0) == 1:
        new_val = [n for n in range(1, 10) if n not in sdk[i]]
        sdk[i][j] = new_val[0]

    if sdk[i][j] == 0:
        cols = []
        for row in range(9):
            cols.append(sdk[row][j])
        if cols.count(0) == 1:
            new_val = [n for n in range(1, 10) if n not in cols]
            sdk[i][j] = new_val[0]

    if sdk[i][j] == 0:
        squ = []
        for row in range(3):
            for col in range(3):
                new_r = (i // 3) * 3 + row
                new_c = (j // 3) * 3 + col
                squ.append(sdk[new_r][new_c])
        if squ.count(0) == 1:
            new_val = [n for n in range(1, 10) if n not in squ]
            sdk[i][j] = new_val[0]

    for garo in range(9):
        if garo == j:
            continue
        if sdk[i][garo] == 0:
            solve(i, garo)

    for sero in range(9):
        if sero == i:
            continue
        if sdk[sero][j] == 0:
            solve(sero, j)

    for row in range(3):
        for col in range(3):
            if (row, col) == (0, 0):
                continue

            new_r = (i // 3) * 3 + row
            new_c = (j // 3) * 3 + col
            if sdk[new_r][new_c] == 0:
                solve(new_r, new_c)


sdk = [[int(n) for n in input().split(' ')] for _ in range(9)]
for i in range(9):
    for j in range(9):
        if sdk[i][j] == 0:
            solve(i, j)
for row in sdk:
    print(' '.join(map(str, row)))
