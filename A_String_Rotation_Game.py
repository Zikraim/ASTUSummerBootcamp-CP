t = int(input())
for i in range(t):
    n=int(input())
    s= input()
    ans=0
    for i in range(len(s)):
        r = s[i:] + s[:i]

        count = 1
        for j in range(len(s)-1):
            if r[j]!=r[j+1]:
                count +=1
        ans= max(ans,count)
    print (ans)
