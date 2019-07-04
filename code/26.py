n=int(input())
d=[int(i) for i in input().split(None,n) [:n]]
f=0
while(f<len(d)):
    o=0
    for i in d:
        while(d[f]<i):
            temp=i
            d[o]=d[f]
            d[f]=temp
        o+=1
    f+=1
print(d)   
