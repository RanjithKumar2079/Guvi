n,q=map(int,input().split(" "))
for g in range(n+1,q):
    count=1
    for i in range(2,g):
    	if(g%i==0):
    		count+=1
    if(g==1 or g==0):
    	pass
    elif(count<=1):
    	print(g)
    else:
    	pass
