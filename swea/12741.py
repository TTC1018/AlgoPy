T = int(input())

answer = ''
for test_case in range(1, T + 1):
    A, B, C, D = map(int, input().split())

    overlay = max(0, min(B, D) - max(A, C))
    answer += '#{} {}\n'.format(test_case, overlay)
print(answer[:-1])