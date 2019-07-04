n=int(input())
q=list(map(int,input().split(None,n)[:n]))
for i in q:
    print(i,q.index(i))
