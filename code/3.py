n=input()
if(len(n)==1 and !(n.isdigit())):
      if(n in ["a","e","i","o","u","A","E","I","O","U"]):
              print("Vowel")
      else:
              print("Consonant")
else:
      print("invalid")
