T = int(input())
answer = ''
for test_case in range(1, T + 1):
    A, B = map(int, input().split())

    time = (A + B) % 24
    answer += '#{} {}\n'.format(test_case, time)
print(answer[:-1])