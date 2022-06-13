from math import ceil
import sys
input = sys.stdin.readline


def battle(type, r_a, r_h, max_hp):
    global hp, attack

    if type == 1:
        hit_to_kill = ceil(r_h / attack)
        hp -= (r_a * (hit_to_kill - 1))
        if hp > 0:
            return True
        else:
            return False
    elif type == 2:
        attack += r_a
        hp = min(max_hp, hp + r_h)
        return True

# 용사의 조건 충족 최소 HP 구하기
# 방은 순차적으로 이동
N, Hatk = map(int, input().split())
room = []
end = 0
for _ in range(N):
    t, a, h = map(int, input().split())
    room.append((t, a, h))
    if t == 1:
        end += (a * ceil(h / Hatk))

answer = 1
start = 1
while start <= end:
    mid = (start + end) // 2

    hp, attack = mid, Hatk
    for t, a, h in room:
        if not battle(t, a, h, mid): # 중도 사망
            start = mid + 1
            break
    else: # 클리어
        answer = mid
        end = mid - 1
print(answer)