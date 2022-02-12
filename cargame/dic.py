from collections import defaultdict
b=input().split()
k=0
a={"a","b","c","d","e","f","g","h","i","j","k","l","m",
     "n","o","p","q","r","s","t","u","v","w","x","y","z"}
d = dict.fromkeys(a, [])
for i in b:
     d[i].append(k)
     k+=1
for i in b:
    print(d[i])
