N = int(input())

students = [[] for _ in range(N)]
for i in range(N):
    name, k, e, m = input().split()
    k, e, m = map(int, [k, e, m])
    students[i].extend([name, k, e, m])
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(students[i][0])