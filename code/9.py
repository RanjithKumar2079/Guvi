n,k=map(int,input().split(" "))
arr=[int(i) for i in input().split()]
s=0
for i in range(k):
	s=s+arr[i]
print(s)
