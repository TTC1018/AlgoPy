S = input()

s_alpha = [n for n in S if ord(n) >= 65]
s_digit = [int(n) for n in S if ord(n) < 65]
digit_sum = sum(s_digit)

s_alpha.sort()
print(''.join(s_alpha) + str(digit_sum))