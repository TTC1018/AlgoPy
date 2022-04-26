import sys
input = sys.stdin.readline().rstrip


target = list(input())
t_len = len(target)

palin = [[False] * t_len for _ in range(t_len)]
for i in range(t_len):
    palin[i][i] = True
for i in range(t_len - 1):
    if target[i] == target[i + 1]:
        palin[i][i + 1] = True
for i in range(2, t_len):
    for j in range(t_len - i):
        if target[j] == target[j + i] and palin[j + 1][j + i - 1]:
            palin[j][j + i] = True

INF = int(1e9)
dp = [INF] * t_len
dp[0] = 1
for i in range(1, t_len):
    dp[i] = dp[i - 1] + 1 # 초기화 (한자리 수 팰린드롬 붙인 것)
    for j in range(i):
        if palin[j][i]:
            if j == 0: # index 0..i까지 팰린드롬이므로 문자열 자체가 팰린드롬
                dp[i] = 1
                break # 이것보다 더 작은 수가 나올 수 없음
            else:
                dp[i] = min(dp[i], dp[j - 1] + 1) 
                # index j..i까지 팰린드롬이라면
                # dp[j - 1]까지 카운트 된 팰린드롬 + j..i팰린드롬 1개의 수를 현재값과 비교
print(dp[-1])