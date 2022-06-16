import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

cnt = 0
b_cnt = [0] * (1000000 + 1)
for i in range(N):
    if b_cnt[H[i]]: # 이전 화살로 깰 수 있음
        b_cnt[H[i]] -= 1
    else: # 화살 쏴야됨
        cnt += 1
    b_cnt[H[i] - 1] += 1 # 다음 차례로 깰 수 있는 풍선을 기록해둠
print(cnt)