n=7
a=1
b=0
for i in range (0,n):

    if n%a==0: 
        b=b+1
    a=a+1
if b<=2:
    print (n,"is prime number")
else:
    print (n,"is not a prime number")

