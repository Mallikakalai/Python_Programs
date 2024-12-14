#Sum of first and last digit of an integer
a=input("Enter the number:")
x=str(a)
y=list()
if len(a)>1:
    for i in x:
        y.append(int(i))
    sumdigi=y[0]+y[-1]
    print (sumdigi)
else:
    print(a)
