n=20
a=1
c=1
for k in range (0,n):
    for i in range(0,n-a):
        print(" ",end="")
    for j in range(0,a):
        print(c,end=" ")
    c=c+1
    a=a+1
    print ()