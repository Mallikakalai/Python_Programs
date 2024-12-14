#write a python code using Lambda function to check every element of a list is an integer or string
list1 = ["abc", 2,3,4,5,"god",7,8,"leaf",10]
result= list(map(lambda x: (x,"Integer") if type(x)==int else (x,"String"),list1))
print(result)

#tried another one - checked each element and added them to separate list
integerlist = list(filter(lambda a: type(a)==int,list1))
stringlist = list(filter(lambda b: type(b)==str, list1))
print (integerlist)
print (stringlist)