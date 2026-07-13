for i  in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l=0
    r=n-1
    count=0
    while l<r:
        if a[l]==1 and a[r]==0:
            count+=1
            l+=1
            r-=1
        elif a[l] ==0:
            l+=1
        else: 
            r-=1
      
    print(count)
