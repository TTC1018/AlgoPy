import sys
input = sys.stdin.readline


X = int(input())
stick = 1<<6 # 2^6 = 64
shortest = stick

count = 1
while stick != X:
    half = shortest >> 1 # 가장 짧은 막대 쪼개기
    stick -= half # 일단은 버린다고 가정
    
    if stick < X: # 버렸을 때 X보다 작으면 (크거나 같은 경우가 아니면)
        stick += half # 버린 거 취소
        count += 1 # 막대 개수 카운트
    shortest = half # 가장 짧은 막대 갱신
print(count)