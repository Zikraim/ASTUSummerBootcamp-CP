n,m=list(map(int,input().split()))
a=[0]+list(map(int,input().split()))
pref=[0]*(n+1)
for i in range(1,n):
     if a[i]-a[i+1]>0:
          pref[i+1]=pref[i]+(a[i]-a[i+1])
     else:
          pref[i+1]=pref[i]
suf=[0]*(n+1)
for i in range(n,1,-1):
     if a[i]-a[i-1]>0:
          suf[i-1]=suf[i]+(a[i]-a[i-1])
     else:
          suf[i-1]=suf[i]  
for _ in range(m):                          
   s,t=map(int,input().split())

   if s<t:
        print(pref[t]-pref[s])
   else:
     print(suf[t]-suf[s])   
