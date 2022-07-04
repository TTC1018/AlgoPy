import sys
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    A.sort()

    answer = 1
    end = A[0][1]

    for i in range(1, N):
        if end > A[i][1]:
            end = A[i][1]
            answer += 1
    print(answer)
