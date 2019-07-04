n,q=map(int,input().split(" "))
for i in range(n+1,q):
    re=0
    j=i
    while(i>0):
        x=i%10
        re=re+pow(x,3)
        i=i//10
    if(re==j):
        print(j)
    else:
        pass
