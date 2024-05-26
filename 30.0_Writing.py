# File Handling... > writing in a file

f=open("File1.text","w") # w will erase the content if file present,if not it create file
statement=input("Enter some text  >> ")
f.write(statement)   # write fun can takes only one string "......."
f.close()
