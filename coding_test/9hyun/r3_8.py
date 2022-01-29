import time

S = input()

start = time.time()
s_alpha = [n for n in S if ord(n) >= 65]
s_digit = [int(n) for n in S if ord(n) < 65]
# s_alpha = [n for n in S if n.isalpha()]
# s_digit = [int(n) for n in S if n not in s_alpha]
end = time.time()
print(end - start)

digit_sum = sum(s_digit)

s_alpha.sort()
print(''.join(s_alpha) + str(digit_sum))