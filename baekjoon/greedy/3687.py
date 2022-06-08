import sys
input = sys.stdin.readline
# 2개 : 1, 3개 : 7, 4개 : 4, 5개 : 2 3 5, 6개 : 6 9 0, 7개 : 8
# 0으로 시작 불가
cnt_dict = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}
dp_s = [sys.maxsize] * (100 + 1)
big = [0] * 101

# 초기화
for key in cnt_dict:
    min_val = min(cnt_dict[key])
    dp_s[key] = min_val if min_val != 0 else cnt_dict[key][1]
    big[key] = max(cnt_dict[key])

# 최솟값 구하기 (DP)
for i in range(7, 101):
    for key in cnt_dict:
        if key > i:
            break

        target = str(dp_s[i - key])
        added = min(cnt_dict[key])
        dp_s[i] = min(dp_s[i], int(target + str(added)))

# 최댓값 구하기
for i in range(4, 101):
    if not i % 2: # 짝수면 싹 다 1써서 자릿 수 늘리기
        big[i] = int('1' * (i // 2))
    else: # 홀수면 맨 첫자리 7, 나머지 다 1쓰기
        big[i] = int('7' + '1' * ((i - 3) // 2))


for _ in range(int(input())):
    n = int(input())
    print(dp_s[n], big[n])
