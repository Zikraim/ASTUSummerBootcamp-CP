t= int(input())
for i in range(t):
    n= int(input())
    s= input()
    ans=0
    last=s[-1]
    for i in range(len(s)-1,-1,-1):
        if last!=s[i]:
            ans+=1
    print(ans)
