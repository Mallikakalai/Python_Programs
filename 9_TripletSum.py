#find the triplet in the list whose sum is 59
a=[10,20,30,9]
f=0
for i in range(len(a)):
    if f==1:
        break
    for j in range(1,len(a)):
        if f==1:
            break
        for k in range(2,len(a)):
            if (a[i]+a[j]+a[k])==59:
                print ("The Triplets are:" ,a[i],a[j],a[k])
                f=f+1
                break
                
        


    


