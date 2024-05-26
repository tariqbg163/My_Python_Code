# Reading a specific number of characters
f=open("File1.text","r")
print(f.read(8)) # read first 8 characters from the file
f.close()

print("Printing single line....")
# Reading a single line from a file one each call

f2=open("File2.text", "r")
print(f2.readline()) # print ist line
print(f2.readline()) # print 2nd line
f2.close

# printing all lines of a file
f3=open("File2.text", "r")
print(f3.readlines())  # it return a list 
f3.close()

# We can read all lines of a file using for loop.
# for loop will execute to the of lines in a file

f4=open("File2.text","r")
for line in f4:           # line = loop variable
    print(line)
f4.close()
