n,a,d=map(int,input().split(" "))
r=[]
for i in range(1,n+1):
    r.append(a)
    a=a+d
s=0
for i in r:
    s=s+i
print(s)
