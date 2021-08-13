n = int(input())
A, B, C, D = [0] * n, [0] * n, [0] * n, [0] * n
for i in range(n):
    A[i], B[i], C[i], D[i] = map(int, input().split(' '))
A.sort()
B.sort()
C.sort()
D.sort()

ac, bc, cc, dc = 0, 0, 0, 0
answer = 0
while ac < n and bc < n and cc < n and dc < n:
    if A[ac] + B[bc] + C[cc] + D[dc] == 0:
        answer += 1

    

print(answer)
