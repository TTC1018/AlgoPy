import sys
input = sys.stdin.readline


def to_binary(num):
    result = ''
    while num != 0:
        div, mod = divmod(num, 2)
        result += str(mod)
        num = div
    result = result[::-1]
    return result


def to_decimal(str_num):
    result = 0
    s_idx = 0
    s_len = len(str_num)
    for i in range(s_len - 1, -1, -1):
        if int(str_num[s_idx]) != 0:
            result += 2 ** i
        s_idx += 1
    return str(result)


for _ in range(int(input())):
    M, N = input().split()
    M = int(M)

    if M == 1:
        N = N.split('.')  # 8개
        binary = ''  # 기본 문자열
        for n in N:  # 8개 순차탐색
            result = to_binary(int(n))  # 이진법 바꾸고
            binary += ('0' * (8 - len(result)) + result)  # 0부족하면 채우고
        decimal = to_decimal(binary)
        print(decimal)
    elif M == 2:
        binary = to_binary(int(N))
        binary = '0' * (64 - len(binary)) + binary
        ipv8 = ''
        for i in range(0, len(binary), 8):
            ipv8 += to_decimal(binary[i:i + 8])
            ipv8 += '.'
        ipv8 = ipv8[:-1]  # '.' 제거
        print(ipv8)
