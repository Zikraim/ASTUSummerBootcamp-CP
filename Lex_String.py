t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    a=sorted(input(),reverse=True)
    b=sorted(input(),reverse=True)
    c=[]
    count_a=0
    count_b=0
    while a and b:
        if (a[-1]<b[-1]) and(count_a<k) or count_b==k:
            c.append(a.pop())
            count_a+=1
            count_b=0
        else:
            c.append(b.pop())
            count_b+=1
            count_a=0
    print("".join(c))
