#Palindrome - return Tue or False
a=input("Enter the string: ")
a=a.lower()
if a==a[::-1]:
    print("True")
else:
    print("False")

