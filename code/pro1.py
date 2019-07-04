n=int(input())
j=[]
t=[]
for i in range(n):
    j.append(input())
r=0
for i in j[0]:
    if(i==j[1][r]):
        t.append(i)
    elif(i!=j[1][r]):
        break
    r=r+1
print(*t,sep="")
