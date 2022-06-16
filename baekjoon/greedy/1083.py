import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
S = int(input())


for i in range(N - 1):
    max_val = A[i]

    cnt = 0
    # 현재 인덱스에서 시작하여
    # 남은 교환 횟수 만큼의 범위 내에 있는 수 중에
    # 가장 큰 수를 찾아서 현재 수와 바꾸기 (자신보다 큰 수 없으면 안 바꿈)
    for j in range(i + 1, min(i + 1 + S, N)):
        diff = j - i
        if A[j] > max_val:
            max_val = A[j]
            cnt = diff

    if cnt:
        S -= cnt
        A.remove(max_val)
        A.insert(i, max_val)

    if not S:
        break

print(*A)