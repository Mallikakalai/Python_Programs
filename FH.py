
with open("C:\\Users\\AM9131\\Documents\\FileHand.txt", 'r') as file:
    lines = file.readlines()
lines.insert(3, "Mallika" + '\n')
with open("C:\\Users\\AM9131\\Documents\\FileHand.txt", 'w') as file:
        file.writelines(lines)
f = open("C:\\Users\\AM9131\\Documents\\FileHand.txt","r")
print(f.read())






# with open("C:\\Users\\AM9131\\Documents\\FileHand.txt", "r") as f:
    # contents = f.readlines()
# contents.insert(2,"Mallika")
# with open("C:\\Users\\AM9131\\Documents\\FileHand.txt", "w") as f:
    # f.writelines(contents)
 
   
    






# f = open("C:\\Users\\AM9131\\Documents\\FileHand.txt","a")
# f.write("K adding new line")
# f.close()
# f = open("C:\\Users\\AM9131\\Documents\\FileHand.txt","r")
# print(f.read())