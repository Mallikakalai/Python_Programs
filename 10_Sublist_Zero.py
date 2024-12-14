#find if there is a sublist with the sum equals to Zero
a=[4,2,-3,1,6]
b=list()
f=0
for i in range (len(a)):
    b.append(a[i])
    for j in range (1,len(a)):
        b.append(a[j])
        for k in range(2,len(a)):
            b.append(a[k])
            if sum(b)==0:
                print (b)
                break
            else:
                b.clear()