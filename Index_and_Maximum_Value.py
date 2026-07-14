for _ in range(int(input())):
    n,m= map(int, input().split())
    arr=list(map(int, input().split()))
    maxi=[]
    currentmax=max(arr)
    for _ in range(m):
         c, l_str, r_str = input().split()
         l, r = int(l_str), int(r_str)
        
         if l<=currentmax<=r:
             if c=="+":
               currentmax+=1
             else:
                 currentmax-=1
         maxi.append(currentmax)
           
    print(*maxi)
           
             
        



