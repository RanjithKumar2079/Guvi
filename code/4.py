n=input()
if(len(n)==1):
    n=n.upper()
    if(n>="A" and n<="Z"):
        print("Alphabet")
    else:
        print("No")
else:
    print("No")
