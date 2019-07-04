h1,m1=map(int,input().split(" "))
h2,m2=map(int,input().split(" "))
tm1=(h1*60)+m1
tm2=(h2*60)+m2
to=max(tm1,tm2)-min(tm1,tm2)
m=to%60
h=to//60
print(h,m)
