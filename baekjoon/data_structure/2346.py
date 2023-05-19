from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
B = deque(list(enumerate(list(map(int, input().split())))))

answer = []
while B:
    idx, num = B.popleft()
    answer.append(idx + 1)

    if num > 0:
        B.rotate(-(num - 1))
    else:
        B.rotate(-num)
    print(*B)
print(*answer)