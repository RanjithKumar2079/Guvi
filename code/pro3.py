e,q=map(str,input().split(" "))
q=list(q)
e=list(e)
count=0
while(len(q)>len(e)):
    q.pop()
    count+=1
for i in range(len(q)):
    if(q[i]!=e[i]):
        q[i]=e[i]
        count+=1
print(count)
