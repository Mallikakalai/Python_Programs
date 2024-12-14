#To find first non-repeating element
a=[2,2,3,3,4,4,5,6,6,8,8,9]
b=[]
for i in a:
    x=a.count(i)
    if x==1:
        b.append(i)
print("First non-repeating element", b[0])
