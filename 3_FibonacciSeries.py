#Using the python lambda function create a Fibonacci series from 1 to 50 elements 
#since the question is not clear generated 2 outputs
from functools import reduce
#created list to generate the fibonacci series
fiblist=[1,1] 
#geneate series till 50 hence created a loop with that criteria
while fiblist[-1]<=50: 
    fibonacciseries=reduce((lambda x,y:fiblist[-2]+fiblist[-1]),fiblist) #from the list the last 2 list elements will be added and stored in the variable used lambda and reduce for this operation
    if fibonacciseries>=50: 
        break
    else:
        fiblist.append(fibonacciseries) 
print("Output 1 = ",fiblist)

#if the question is to print 50 elements, used for loop to append 50 elements in the list
fiblist1=[1,1]
for i in range(1,50):
    fibonacciseries1=reduce((lambda x,y:fiblist1[-2]+fiblist1[-1]),fiblist1) #from the list the last 2 list elements will be added and stored in the variable used lambda and reduce for this operation
    fiblist1.append(fibonacciseries1) 
print("Output 2 = ",fiblist1)