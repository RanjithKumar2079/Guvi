n=input()
t=False
for i in n:
    if i in ["1","2","3","4","5","6","7","8","9","0","."]:
        z=n.count(".")
        if(z>1):
            t=False
        else:
            t=True
    else:
        t=False
    if(t==False):
        break
if(t==True):
    print("yes")
else:
    print("no")
