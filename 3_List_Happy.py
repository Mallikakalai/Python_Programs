a=[10,501,22,37,100,999,87,351]
for i in a: 
    n=i
    while n>=10:
        sum=0
        while n>0:
            lastdigit=n%10
            sum=sum+(lastdigit**2)
            n=n//10
            print (sum)
        n=sum
    if n==1:
        print(i," is a happy number")
    else:
        print (i, "is not a happy number")

    
    
    





        




