import sys


N, K = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, list(sys.stdin.readline().rstrip())))

q = []
for i in range(N):
    while K > 0 and q and q[-1] < num[i]: # 현재 들어갈 수보다 작은 수들을 스택에서 제거
        q.pop()
        K -= 1
    q.append(num[i])

while K > 0: # 내림차순 삽입 혹은 같은 값의 수 반복 등으로 덜 제거 됐을 때
    K -= 1
    q.pop() # 맨 뒤에 수 제거
print(''.join(map(str, q)))