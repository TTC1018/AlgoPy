import sys
input = sys.stdin.readline


N = int(input())
W = list(map(int, input().split()))
W.sort()

if W[0] > 1:
    print(1)
else:
    # 현재 무게추 리스트가 값 X까지 커버할 수 있을 때
    # 새로운 무게추 A가 추가되면, X + A 까지의 무게를 커버할 수 있다 (1이 있는 경우에)
    # 예) {1, 1, 2} => 1, 2, 3, 4 커버 가능
    # A = 3 -> 1 + 3, 2 + 3, 3 + 3, 4 + 3 = 4, 5, 6, 7 커버 가능해짐
    # 만약 A = 5일 때,
    # 1 + 5, 2 + 5, 3 + 5, 4 + 5 = 6, 7, 8, 9 커버 가능 -> 5라는 비는 공간이 생김
    # 즉, 빈 공간 없이 커버하려면 현재 누적합 보다 적은 수의 무게추가 추가 되어야 함
    sum = 1 # 누적합에 + 1 되어 있는 변수
    for i in range(N):
        if sum < W[i]: # 현재 누적합 + 1을 뛰어넘는 무게추가 추가될 때
            break
        sum += W[i]
    print(sum)