n=int(input())
j=[]
t=[]
for i in range(n):
    j.append(input())
r=0
k=min(j)
for i in k:
    if(i==j[r][r]):
        t.append(i)
    elif(i!=j[r][r]):
        break
    r=r+1
print(*t,sep="")
