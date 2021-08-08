def generate_cand(i, j):

    # 불가능한 값은 후보군에서 제거하는 메소드
    candidate = [n for n in range(1, 10)]
    for col in sdk[i]:
        if col in candidate:
            candidate.remove(col)
    for row in range(9):
        if sdk[row][j] in candidate:
            candidate.remove(sdk[row][j])
    for row in range((i // 3) * 3, (i // 3) * 3 + 2 + 1):
        for col in range((j // 3) * 3, (j // 3) * 3 + 2 + 1):
            if sdk[row][col] in candidate:
                candidate.remove(sdk[row][col])

    return candidate


def solve(depth):
    global end_flag

    if end_flag:
        return

    if depth == len(points): # 답까지 도달한 값들만이 함수를 종료시킬 수 있음
        end_flag = True
        for row in sdk:
            print(*row)
        return
    else:
        i, j = points[depth]
        candidate = generate_cand(i, j)
        for c in candidate:
            sdk[i][j] = c # 답이 아닌 값이 전달될 시에, 결국에는 candidate가 빈 리스트가 됨. 그것이 break의 역할을 해줌
            solve(depth + 1)
            sdk[i][j] = 0


sdk = [[int(n) for n in input().split(' ')] for _ in range(9)]
points = [(i, j) for i in range(9) for j in range(9) if sdk[i][j] == 0]

end_flag = False
solve(0)