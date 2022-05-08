for case in range(int(input())):
    A, B = map(int, input().split())

    print('#{}'.format(case), end=' ')
    if A <= 9 and B <= 9:
        print(A*B)
    else:
        print(-1)