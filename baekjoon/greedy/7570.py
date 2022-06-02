import sys
input = sys.stdin.readline


N = int(input())
num = list(map(int, input().split()))
idx = [0] * (N + 1) # 숫자 n이 idx[i]번째에 있음을 기록
for i in range(N):
    idx[num[i]] = i

length = 0
lis = 1
for i in range(1, N):
    if idx[i] < idx[i + 1]: # n과 n + 1의 위치를 비교, n + 1이 더 뒤에 있으면 조건 충족 (연속하는 수로만 이루어진 증가수열)
        lis += 1
        length = max(length, lis)
    else: # 증가수열이 아니거나, 증가수열이지만 연속하는 숫자로만 이루어진 증가수열이 아닌 경우
        lis = 1
print(N - length)