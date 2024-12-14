#Create a Even  number list and another list with odd numbers
a=[10,501,22,37,100,999,87,351]
b=list()
c=list()
for i in range (len(a)):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
print ("Even List:", b)
print ("Odd List:", c)