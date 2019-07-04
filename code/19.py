n=int(input())
if(n==0):
    print(1)
elif(n>0):
    s=1
    for i in range(1,n+1):
        s=s*i
    print(s)
else:
    pass
