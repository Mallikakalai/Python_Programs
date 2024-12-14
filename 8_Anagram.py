#Anagram
a=input ("Enter the 1st String: ")
b=input ("Enter the 2nd String: ")
a=a.lower()
b=b.lower()
x=list()
y=list()
for i in a:
    x.append(i)
for k in b:
    y.append(k)
x.sort()
y.sort()
if x==y:
    print ("True")
else:
    print ("False")
