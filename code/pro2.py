from itertools import combinations
q,e=map(str,input().split(" "))
w=[]
for i in q:
    w.append(int(i))
a1=len(w)-int(e)
a=combinations(w,a1)
re=[]
for i in a:
    o=""
    for j in i:
        o=o+str(j)
    re.append(int(o))
re.sort()
print(re[0])
