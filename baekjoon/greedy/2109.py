import sys
input = sys.stdin.readline

n = int(input())
pay = [list(map(int, input().split())) for _ in range(n)]
pay.sort(key=lambda x:-x[0])

answer = 0
checked = [False] * 10001
for i in range(n):
    for j in range(pay[i][1], 0, -1):
        if not checked[j]:
            checked[j] = True
            answer += pay[i][0]
            break
print(answer)