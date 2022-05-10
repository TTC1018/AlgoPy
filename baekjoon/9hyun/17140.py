from collections import Counter
import sys
input = sys.stdin.readline


def R():
    new_A = []
    longest = 0
    for a in A:
        new_row = []
        A_counter = Counter(a)
        del A_counter[0] # 0은 카운트 X

        c_list = A_counter.most_common()
        c_list.sort(key= lambda x:(x[1], x[0]))
        if len(c_list) > 50: # 튜플이니까 100 / 2 = 50
            c_list = c_list[:50]

        for new_content in c_list:
            new_row.extend(list(new_content))

        longest = max(longest, len(new_row)) # 가장 긴 행 길이 갱신
        new_A.append(new_row)

    for i in range(len(new_A)):
        if len(new_A[i]) < longest:
            while len(new_A[i]) != longest:
                new_A[i].append(0)

    return new_A


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

r, c = r - 1, c - 1
for sec in range(100 + 1):
    if r < len(A) and c < len(A[0]):
        if A[r][c] == k:
            print(sec)
            sys.exit()

    r_len, c_len = len(A), len(A[0])
    if r_len >= c_len:
        A = R()
    else:
        A = list(map(list, zip(*A))) # 행,열 뒤집기
        A = R()
        A = list(map(list, zip(*A))) # 원상복구

print(-1)