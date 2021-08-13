from itertools import combinations

N, S = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

num1, num2 = nums[:len(nums) // 2], nums[len(nums) // 2:] # 기존 수열을 좌, 우로 나누기 (최대 2^40 보다 최대 2^20 * 2가 낫기 때문)
sum1, sum2 = [], []
for i in range(len(num1) + 1):
    for c in combinations(num1, i):
        sum1.append(sum(c))
for i in range(len(num2) + 1):
    for c in combinations(num2, i):
        sum2.append(sum(c))

sum1.sort()
sum2.sort()
answer = 0
len1, len2 = len(sum1), len(sum2)
left, right = 0, len2 - 1
while left < len1 and 0 <= right:
    temp_sum = sum1[left] + sum2[right]

    if temp_sum == S: # 원하는 값일 때
        ls, rs = 1, 1 # 수열들이 이미 정렬되어 있으므로, 같은 값을 갖는 대상들을 미리 계산
        l_sav, r_sav = left, right
        left += 1
        while left < len1 and sum1[left] == sum1[l_sav]: # 좌측 수열에서 같은 값을 갖는 대상
            ls += 1
            left += 1
        right -= 1
        while 0 <= right and sum2[right] == sum2[r_sav]: # 우측 수열에서 같은 값을 갖는 대상
            rs += 1
            right -= 1
        answer += ls * rs # 조합이므로 곱하기
    elif temp_sum < S:
        left += 1
    else:
        right -= 1

if S == 0:
    print(answer - 1)
else:
    print(answer)