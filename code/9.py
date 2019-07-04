n,k=map(int,input().split(" "))
arr=[int(i) for i in input().split(None,n) [:n]]
s=0
for i in range(k):
	s=s+arr[i]
print(s)
