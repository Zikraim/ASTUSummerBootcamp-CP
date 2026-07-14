t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    arr = []

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            arr.append(i)

    if not arr:
        print("Yes")
    elif arr[-1] - arr[0] + 1 == len(arr):
        print("Yes")
    else:
        print("No")
