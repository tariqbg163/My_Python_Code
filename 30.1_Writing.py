# writting multiple lines in a file
city=["Peshawar\n","Karachi\n","Islamabad \n","Lahore \n"]
f=open("File2.text","w")
f.writelines(city)  # writelines fun takes multiple (list) string lines "...", "..","..."
f.close()