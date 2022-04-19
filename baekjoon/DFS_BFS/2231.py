N = int(input())
answer = [0] * (N + 1)

flag = False
for i in range(1, N + 1):
    answer[i] = i + sum(map(int, str(i)))
    if answer[i] == N:
        print(i)
        flag = True
        break

if not flag:
    print(0)