def dfs(num, index):
    if index == N:
        result.append(num)
        return

    for j in range(1, 4 + 1):
        if oper[j] != 0:
            oper[j] -= 1
            if j == 1: # +
                dfs(num + A[index], index + 1)
            elif j == 2: # -
                dfs(num - A[index], index + 1)
            elif j == 3: # *
                dfs(num * A[index], index + 1)
            elif j == 4: # c++ div
                dfs(cpp_div(num, A[index]), index + 1)
            oper[j] += 1


def cpp_div(a, b):
    if a >= 0:
        return a // b
    else:
        a = -a
        return -(a // b)


N = int(input())
A = list(map(int, input().split()))
oper = {1: 0, 2: 0, 3: 0, 4: 0}
# 1: +, 2: -, 3: *, 4: //
for i, o in enumerate(map(int, input().split())):
    oper[i + 1] += o

result = []
dfs(A[0], 1)
print(max(result))
print(min(result))