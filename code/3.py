n=input()
d=True
if n in ["[","@","_","!","#","$","%","^","&","*","(",")","<",">","?","/","\\","|","}","{","~",":","]"]:
	d=False
if(len(n)==1 and not(n.isdigit()) and d):
      if(n in ["a","e","i","o","u","A","E","I","O","U"]):
              print("Vowel")
      else:
              print("Consonant")
else:
      print("invalid")
