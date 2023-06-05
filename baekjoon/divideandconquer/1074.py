import sys

input = sys.stdin.readline


def divide(x, y, width):
    global answer

    if x > r or x + width <= r or y > c or y + width <= c:
        answer += width ** 2
        return

    if width <= 2:
        if x == r and y + 1 == c:
            answer += 1
        elif x + 1 == r and y == c:
            answer += 2
        elif x + 1 == r and y + 1 == c:
            answer += 3
        print(answer)
        exit()
    else:
        width //= 2
        divide(x, y, width)
        divide(x, y + width, width)
        divide(x + width, y, width)
        divide(x + width, y + width, width)


N, r, c = map(int, input().split())
answer = 0
divide(0, 0, 2 ** N)
