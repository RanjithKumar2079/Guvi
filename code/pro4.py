e,q=map(str,input().split(" "))
q=list(q)
e=list(e)
count=0
while(len(q)>len(e)):
    x=q.pop()
    count+=(abs(ord('a')-ord(x))+1)
for i in range(len(q)):
    if(q[i]!=e[i]):
        count+=abs((ord(q[i])-ord(e[i])))
        q[i]=e[i]
print(count)
