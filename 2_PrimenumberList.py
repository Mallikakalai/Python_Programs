#Count a prime and create a list with all the prime numbers
a=[10,501,22,37,100,999,87,351]
c=2
b=list()
for i in a:
    q=0
    for j in range (2,i):
        if i%j==0:
            q=q+1
    if q<2:
        b.append(i)
print ("Number of prime numbers:", len(b))
print (b)
