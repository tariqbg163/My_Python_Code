# reading from file.. if file not exist if cause error
f=open("File1.text", "rt")  # r of reading and t of text .. t is optional
print(f.read())
f.close()

f2=open("File2.text", "rt")
city=f2.read()  # return a string
f.close()
print("City = ", city)
print("Type of city = ", type(city))

