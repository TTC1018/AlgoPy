import sys
input = sys.stdin.readline

apartment = [[i for i in range(14 + 1)] for _ in range(14 + 1)]
for i in range(1, 14 + 1):
    for j in range(1, 14 + 1):
        apartment[i][j] = apartment[i][j - 1] + apartment[i - 1][j] if j != 1 else apartment[i - 1][j]

for _ in range(int(input())):
    k, n = int(input()), int(input())
    print(apartment[k][n])