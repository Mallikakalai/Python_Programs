#Find the duplicates in the three lists 
a=[1,2,3,4,5,6,6,6,7,8,8,9]
b=['cat','dog',6,9,9]
c=['dog',1,2]
y=[]
for i in a:
    b.append(i)
for j in c:
    b.append(j)
g=set(b)
for k in g:
    x=b.count(k)
    if x>1:
        y.append(k)
print(y)

