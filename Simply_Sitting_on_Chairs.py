t= int(input())
for _ in range(t):
    n= int(input())
    p= list(map(int,input().split()))
    backward=0
    for i in range(len(p)):
        if p[i] <= i+1:
            backward+=1
    print(backward)
