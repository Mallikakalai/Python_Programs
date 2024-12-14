#Function to read from a text file. 
#The function will take the name of the text file and display the content of the file into the console

#take the name of the file
f=open(input("Enter the file name"),"r")

#read and display the content of the file
print(f.read())

#close the file
f.close()

