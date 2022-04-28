import sys
input = sys.stdin.readline
# 최상위 비트는 무조건 1 (두자리 수 부터)
# 자릿 수에 2^N개 만큼 1을 추가시킴
# 예) 2자리 -> 10, 11 = 최상위 비트1 2개
# 3자리 -> 100, 101, 110, 111 = 최상위 비트1 4개
# N자리 수 1의 개수 = N-1자리 1의 개수 * 2 + 2^(N - 1)
# N=1 : 1
# N=2 : 1 0, 1 1
# N=3 : 1 00, 1 01, 1 10, 1 11
# N=4 : 1 000, 1 001, 1 010, 1 011, 1 100, 1 101, 1 110, 1 111
def func(num):
    sum_val = 0
    binary = bin(num)[2:] # 맨앞 0b 제거
    b_len = len(binary)
    
    for i in range(b_len):
        if binary[i] == '1': # 0일 때는 분할 정복할 필요 없음
            cipher = b_len - i - 1
            sum_val += (num - 2**cipher + 1) # 같은 자리 수의 최상위비트 1 개수를 num까지 세기
            sum_val += p_sum[cipher] # 현재 최상위비트 보다 한자리 작은 비트의 1의 개수 총합
            num -= 2**cipher # 최상위 비트 제거
    return sum_val
            

A, B = map(int, input().split())
p_sum = [0] * 55 # 2^53 < 10^16 < 2^54
for i in range(1, 54 + 1):
    p_sum[i] = 2 * p_sum[i - 1] + 2**(i - 1)
print(func(B) - func(A - 1))