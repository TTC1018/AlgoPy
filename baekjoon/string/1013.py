import re
import sys
input = sys.stdin.readline

regex = re.compile('(100+1+|01)+')
for _ in range(int(input())):
    target = input().rstrip()
    if regex.fullmatch(target):
        print('YES')
    else:
        print('NO')