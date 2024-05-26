list1=[11,22,33,"Khan"]
print(f' List is = {list1}')
list1.insert(1,"Khan")  # index, element
print("List = ", list1)
list1.append("Shan")    # element  ... added at the last location
print("List = ", list1)
if "Khan" in list1:
    print("Yes Khan is the member of list1")
    
print("11 is repeated = ", list1.count(33)) # count(element)
print("Index of Khan is ", list1.index("Khan"))  #index(element) return of ist occrence

list1.extend([88,99,00]) # we can pass a sequence or already Exist list

# list.extend(list) # we can pass a the same list to itself
print("List = ", list1)

# list creating through constructor
list2=list(("Ali","Noor",11,22,33))  # list((sequence))  or list([....])
print("List2 = ", list2)
list3=list(("Khan"))  # is single string is pass it make each character is sequence
print("List3 = ", list3)
