S = input()

one_list = [s for s in S.split('0') if s != '']
zero_list = [s for s in S.split('1') if s != '']

answer = min(len(one_list), len(zero_list))
print(answer)