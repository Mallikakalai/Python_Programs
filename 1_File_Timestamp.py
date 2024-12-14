#create a text file with the current timestamp
#the file content should have the content of the current timestamp

#importing datetime module
from datetime import datetime 
#getting current date and time
current_timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
print("Current Date and Time:",current_timestamp)

#converting time to string
str_current_timestamp = str(current_timestamp)

#naming the file with current timestamp
file_name= str_current_timestamp + ".txt"

print(file_name)

#creating file with the current timestamp
f=open(file_name,"w")
print("File Created:",f.name)

#writing file content the content of the current time stamp 
f.write("Current Time Stamp:"+str_current_timestamp)
f.close()
