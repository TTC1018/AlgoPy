import sys
input = sys.stdin.readline


N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

if crane[0] < box[0]:
    print(-1)
else:
    cnt = 0
    while True:
        if not box:
            break
        for i in range(N):
            for j in range(M):
                if box[j] <= crane[i]:
                    del box[j]
                    M -= 1
                    break
        cnt += 1
    print(cnt)