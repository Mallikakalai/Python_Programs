#write a program to validate the following using Regular Expression
#1.Email Validation
#2.Bangladesh Mobile Number
#3.USA Telephone Number
#4.16 digit Password Validation

import re
#Email Validation
email=input("Enter the email")
pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$"
#starts any character including special character following with "@" any character (and allowed only hyphen) following "." any alphabets (withoutdigits), minimum 2 character
if re.match(pattern,email):
    print("Valid Email")
else:
    print("Invalid Email")

#Bangladesh Mobile Number
#As per wikipedia Typical format for a mobile phone number is 01XXX NNNNNN, e.g. 01054 694200 
BangladeshMobile=input("Enter the mobile number")
patternmobile=r"^01[0-9]{9}$"
#starts with 01 and any 9 digits
if re.match(patternmobile,BangladeshMobile):
    print("Valid")
else:
    print("Invalid")

#USA Telephone Number
USATeleNumber=input("Enter the phone number")
patternUSATele=r"^\(*\d{3}\)*\s*\-*\d{3}-\d{4}$" #can have the following format (123) 675-8976 or (123)675-8976 or 123-456-8907 or 123 789-9870
if re.match(patternUSATele,USATeleNumber):
     print("Valid")
else:
     print("Invalid")


# 16 digit Password Validation 
password=input("Enter the password")
patternpass=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$!#%*?&])[A-Za-z\d@$!%#*?&]{16}$"
#atleast one uppercase, lowercase, special character, digit exact 16 character
if re.match(patternpass,password):
    print("Valid")
else:
    print("Invalid")

