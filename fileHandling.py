
# create a file object with mode "w" for writing and "r" for reading
# if you open file in write mode if file doesnt exist it will create one with the file name passed as first argument
fileObject = open("xyzFile.txt", "w")
# if you open file in read mode and file doesnt exist then the program will throw an error
fileObject2 = open("mnoFile.txt", "r")

# write text in the file xyz.txt pointed by fileObject
for tableOf in range(1, 1001):
    for i in range(1, 11):
        fileObject.write(str(tableOf) + " * " + str(i) + " = " + str(tableOf * i) + "\n")
    fileObject.write("\n\n\n")

# read text from the file mnoFile.txt which is pointed by fileObject2
fileText = fileObject2.read()
print(fileText)

# close the fileobjects
fileObject.close()
fileObject2.close()



