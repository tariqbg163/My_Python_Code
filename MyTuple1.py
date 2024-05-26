# Tuple is ordered and unchangeable
# tuple constructing method 1

t=(11,22,33,11,"Khan","Noor",11)
print(f" tuple t = {t}")

# Accessing tuple elements 
print("t[2] = ", t[2])

print("11 is repeated = ", t.count(11))
print("Index of Khan is ", t.index("Khan"))

# t[2]=666          we can't change tuple elements
# print("t[2] = ", t[2])

# tuple constructing method 2. i.2 tuple(()), or tuple([]), tuple({}), or tuple(collection)
t2=tuple(("Ali","Gul","Ahmad","Shan",111,222))
print("t2 = ", t2)

# Converting tuple into list
t3=list(t2)   # converting list into tuple
print("Type of t3 = ",type(t3))
print("Type of t2 = ", type(t2))
