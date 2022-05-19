def print_up(cube):
    for i in range(3):
        for j in range(3):
            print(cube[2][i][j], end="")
        print()


def rotate(cube, index):
    for _ in range(2):
        temp = cube[index][0][0]
        cube[index][0][0] = cube[index][1][0]
        cube[index][1][0] = cube[index][2][0]
        cube[index][2][0] = cube[index][2][1]
        cube[index][2][1] = cube[index][2][2]
        cube[index][2][2] = cube[index][1][2]
        cube[index][1][2] = cube[index][0][2]
        cube[index][0][2] = cube[index][0][1]
        cube[index][0][1] = temp


def move(cube, direction):
    if direction == 'U':
        temp = cube[0][0]
        cube[0][0] = cube[4][0]
        cube[4][0] = cube[5][0]
        cube[5][0] = cube[3][0]
        cube[3][0] = temp
        rotate(cube, 2)

    elif direction == 'D':
        temp = cube[0][2]
        cube[0][2] = cube[3][2]
        cube[3][2] = cube[5][2]
        cube[5][2] = cube[4][2]
        cube[4][2] = temp
        rotate(cube, 1)

    elif direction == 'F':
        temp = cube[2][2]
        cube[2][2] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
        cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[1][0]
        cube[1][0] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = temp
        rotate(cube, 0)

    elif direction == 'B':
        temp = cube[2][0]
        cube[2][0] = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
        cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[1][2]
        cube[1][2] = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = temp
        rotate(cube, 5)

    elif direction == 'L':
        temp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][2][0], cube[1][1][0], cube[1][0][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = temp
        rotate(cube, 3)

    elif direction == 'R':
        temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = temp
        rotate(cube, 4)


def go(cube, command):
    direction, count = command
    count = 1 if count == '+' else 3
    for _ in range(count):
        move(cube, direction)


for _ in range(int(input())):
    input()
    spin = input().split()
    cube = [[] for _ in range(6)]
    for _ in range(3):
        cube[0].append(['r', 'r', 'r'])
        cube[1].append(['y', 'y', 'y'])
        cube[2].append(['w', 'w', 'w'])
        cube[3].append(['g', 'g', 'g'])
        cube[4].append(['b', 'b', 'b'])
        cube[5].append(['o', 'o', 'o'])
    for s in spin:
        go(cube, s)
    print_up(cube)