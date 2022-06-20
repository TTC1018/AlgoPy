N = int(input())
L = list(map(int, input().split()))

L.sort()
acid = [l for l in L if l > 0]
alc = [l for l in L if l < 0]

if not acid:
    print(alc[-2], alc[-1])
elif not alc:
    print(acid[0], acid[1])
else:
    