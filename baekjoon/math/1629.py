import sys
input = sys.stdin.readline


def pow(a, e):
    if e == 1:
        return a % C

    half = pow(a, e // 2)
    if e % 2 == 1:
        return (a % C) * ((half**2) % C)
    return (half**2) % C



A, B, C = map(int, input().split())
print(pow(A, B) % C)