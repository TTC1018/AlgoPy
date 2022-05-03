from bisect import bisect_left
import sys
input = sys.stdin.readline


N = int(input())
lines = []
for _ in range(N):
    A, B = map(int, input().split())
    lines.append((A, B))
lines.sort() # A 전봇대 기준으로 정렬

sequence = [-1]
idx_list = [-1] * 500001
max_idx = 0

for i in range(N):
    if sequence[-1] < lines[i][1]: # 그대로 증가 수열 만들 수 있으면
        sequence.append(lines[i][1])
        idx_list[lines[i][1]] = len(sequence) - 1
        max_idx = idx_list[lines[i][1]]
    else: # 불가능할 때
        idx_list[lines[i][1]] = bisect_left(sequence, lines[i][1]) # 대체할 수 있는 자리 찾기
        sequence[idx_list[lines[i][1]]] = lines[i][1] # 증가 수열 갱신
sequence.pop(0) # 맨 처음 넣은 -1 제거 해주기

real_sequence = []
for i in range(N - 1, -1, -1):
    if idx_list[lines[i][1]] == max_idx:
        real_sequence.append(lines[i][0])
        max_idx -= 1 # 본 수를 기준으로 다음에 오는 대상 찾기
real_sequence.reverse() # 감소수열이 만들어졌기 때문에 증가수열로 바꿔줌

real_sequence = [n[0] for n in lines if n[0] not in real_sequence]
print(len(real_sequence))
for r in real_sequence:
    print(r)