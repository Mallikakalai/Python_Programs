#Question 5 - You have given a list of N integers which represents the number of mangoes in a bag. Each bag has a variable number of mangoes. There are M number of Guvi students, the task is to distribute mangoes such a way that each student gets one bag. The difference between the number of mangoes in a bag with maximum mangoes and bag with minimum mangoes given to the student is minimum? 
#Couldn't understand the question

n=[3,5,12,9]
sumofmango=sum(n)
guvistudent=5
studentmangobag=sumofmango//guvistudent
print ("Each sudent get minimum mangoes:",studentmangobag)

n.sort()
maximum=n[-1]
minimum=n[0]
difference=maximum-minimum
print (difference)







