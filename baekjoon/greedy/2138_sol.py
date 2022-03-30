INF = int(1e9)
def reverse(strs):
    result = ''
    for s in strs:
        if s == '0':
            result += '1'
        else:
            result += '0'
    return result


N = int(input())

now = input() # 첫번째 스위치 OFF
now2 = reverse(now[:2]) + now[2:] # 첫번째 스위치 ON
target = input()

# 스위치를 작동시키고 지나가면 다시 작동시킬 필요가 없는 것이 핵심
# 또한, 현재 작동시킬 스위치의 자리에 해당하는 전구가 중요한 것이 아니라,
# 한자리 이전에 해당하는 전구가 목표와 일치하는지가 중요함 
# (다시 바꿀 수 없는 자리이기 때문에)
# 그런데, 첫번째 스위치는 한자리 이전에 해당하는 전구가 없기 때문에
# 첫번째 스위치 ON/OFF 여부를 초기 두 상태로 두고 진행하는 것

# 첫번째 스위치 OFF인 경우
answer1 = 0
if now[0] != target[0]:
    now = reverse(now[:3]) + now[3:]
    answer1 += 1
for i in range(2, N):
    if now[i - 1] != target[i - 1]:
        now = now[:i - 1] + reverse(now[i - 1:i + 2]) + now[i + 2:]
        answer1 += 1

# 첫번째 스위치 ON인 경우
answer2 = 1
if now2[0] != target[0]:
    now2 = reverse(now2[:3]) + now2[3:]
    answer2 += 1
for i in range(2, N):
    if now2[i - 1] != target[i - 1]:
        now2 = now2[:i - 1] + reverse(now2[i - 1:i + 2]) + now2[i + 2:]
        answer2 += 1

answer = INF
if now == target:
    answer = min(answer, answer1)
if now2 == target:
    answer = min(answer, answer2)

if answer == INF:
    print(-1)
else:
    print(answer)            