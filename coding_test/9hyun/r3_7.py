N = input()

left = list(map(int, N[:len(N)//2]))
right = list(map(int, N[len(N)//2:]))

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")