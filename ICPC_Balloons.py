for _ in range(int(input())):
    n= int(input())
    s=input()
    count=0
    letter=[]
    for i in range(len(s)):
        if s[i] not in letter:
            count+=2
            letter.append(s[i])
        else:
            count+=1
    print(count)
