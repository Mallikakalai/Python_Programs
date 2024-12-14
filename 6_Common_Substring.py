#Take 2 strings and return the longest common substring
a="mallika valluvan"
b="malli vall van"
c=list()
d=""
e=0
for i in range(len(a)):
    for k in range(len(b)):
        if e<len(a):
            if (a[e]==b[k]):
                d=d+b[k]
                c.append(d)
                e=e+1
            else:
            
                d="" 
                e=i
print("String 1:", a)
print("String 2:", b)
x=max(c,key=len)
print(x)