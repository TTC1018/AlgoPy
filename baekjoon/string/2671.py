import re


target = input()
regex = re.compile('(100+1+|01)+')
if regex.fullmatch(target):
    print('SUBMARINE')
else:
    print('NOISE')