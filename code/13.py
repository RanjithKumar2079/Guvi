n=int(input())
count=1
for i in range(2,n):
	if(n%i==0):
		count+=1
if(n==1 or n==0):
	print("no")
elif(count<=1):
	print("yes")
else:
	print("no")
