# end is paramete in python but not a keyword or fun
#it is used inside the print function to end output with user desire
print("A")
print("B") # by default python print fun takes \n at the end
print("C")
print("....")
# use of end parameter
print("A",end=" ") # it end A with space without \n
print("B")
print("C")
print(".....")

print("A",end="...") # it end A with ... without \n
print("B")
print("C")
print("....")

print("A", end="\n")# by default it take end="\n" parameter by the print fun
print("B")
print("C")
print("...")