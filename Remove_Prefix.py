for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    visited=set()
    count=0
    for i in range(n-1,-1,-1):
        if arr[i]in visited:
            count=i+1
            break
        visited.add(arr[i])
            
    print(count)
