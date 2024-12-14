#Takes a string and return a most frequest character in it
a=input("Enter the String: ")
b=list()
d=""
for i in a:
    b.append(i)
for k in range (len(b)):
    for j in range (1,len(b)):
        if b.count(k)>b.count(j):
            d=b[k]
        else:
            d=b[j]
print(d)
