n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dorm = 0
skippedroom = 0

for x in b:
    while x > skippedroom + a[dorm]:
        skippedroom += a[dorm]
        dorm += 1

    print(dorm + 1, x - skippedroom)
