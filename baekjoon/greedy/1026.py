from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt_dict = defaultdict(int)
for a in A:
    cnt_dict[a] += 1
cnt_dict = sorted(map(list, cnt_dict.items()), key=lambda x: x[0])

B.sort()
answer = 0
for b in B:
    answer += (b * cnt_dict[-1][0])
    cnt_dict[-1][1] -= 1
    if not cnt_dict[-1][1]:
        cnt_dict.pop()
print(answer)
