def generate_cand(i, j):

    candidate = [n for n in range(1, 10)]
    for row in sdk[i]:
        if row in candidate:
            candidate.remove(row)
    for col in range(9):
        if sdk[i][col] in candidate:
            candidate.remove(sdk[i][col])
    for row in range(3):
        for col in range(3):
            new_r = (i // 3) * 3 + row
            new_c = (j // 3) * 3 + col
            if sdk[new_r][new_c] in candidate:
                candidate.remove(sdk[new_r][new_c])

    return candidate


def solve(depth):
    global end_flag

    if end_flag:
        return

    if depth == len(points):
        end_flag = True
        for row in sdk:
            print(' '.join(map(str, row)))
        return
    else:
        i, j = points[depth]
        candidate = generate_cand(i, j)
        for c in candidate:
            sdk[i][j] = c
            solve(depth + 1)
            sdk[i][j] = 0


sdk = [[int(n) for n in input().split(' ')] for _ in range(9)]
points = [(i, j) for i in range(9) for j in range(9) if sdk[i][j] == 0]

end_flag = False
solve(0)