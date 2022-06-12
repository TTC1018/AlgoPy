from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input())  # 가진 주사위 수 N^3
dice = list(map(int, input().split()))
# A B C D E F
#       D
#   E   A   B   F
#       C
dice_dict = {'A': dice[0], 'B': dice[1], 'C': dice[2],
             'D': dice[3], 'E': dice[4], 'F': dice[5]}
t_dict = {'A': [('B', 'C'), ('B', 'D'), ('E', 'C'), ('E', 'D')],
          'B': [('A', 'C'), ('A', 'D'), ('F', 'C'), ('F', 'D')],
          'C': [('A', 'B'), ('A', 'E'), ('F', 'E'), ('F', 'B')],
          'D': [('A', 'B'), ('A', 'E'), ('F', 'B'), ('F', 'E')],
          'E': [('A', 'C'), ('A', 'D'), ('F', 'C'), ('F', 'D')],
          'F': [('B', 'C'), ('B', 'D'), ('E', 'C'), ('E', 'D')]}
# 위 모서리 주사위 = 면 3개
# A : B, C, D, E
# B : A, C, D, F
# C : A, B, E, F
# D : A, B, E, F
# E : A, C, D, F
# F : B, C, D, E

# 그 아래 모서리 = 면 2개
# 나머지 = 면 1개
if N == 1:
    print(sum(dice) - max(dice))
else:
    ts = set()
    for k in t_dict:
        for side1, side2 in t_dict[k]:
            sum_val = dice_dict[k] + dice_dict[side1] + dice_dict[side2]
            ts.add(sum_val)

    ss = set()
    for k in t_dict:
        for side1, side2 in t_dict[k]:
            ss.add(dice_dict[side1] + dice_dict[side2])

    min_num = min(dice)
    three = min(ts)
    two = min(ss)

    surface = three * 4 + two * (N - 2) * 4 + min_num * ((N - 2) ** 2)
    down = two * 4 + min_num * (N - 2) * 4
    print(surface + down * (N - 1))
