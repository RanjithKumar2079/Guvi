n=int(input())
j=[]
t=[]
for i in range(n):
    j.append(input())
r=0
k=min(j)
for i in k:
    for g in j:
        if(i==g[r]):
            t.append(i)
        elif(i!=g[r]):
            break
        r=r+1
print(*t,sep="")
