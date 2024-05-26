k=[]
k.append(20) # append add element at the last index position
k.append(40)
k.append(50)
print(k)
print(k[0])
print(k[1])

#2nd way to add element to list
l=[]
print(l)
l.insert(0,111)# insert(index, value)
l.insert(1,22) # it insert a value at desire index location
l.insert(2,50)
l.insert(101,55) # it will insert at the last location
l.insert(2,80) #it will insert 80 at 2nd index
print(l)

# remove(value) fun remove a value that is pass is an argument
a=[11,12,11,22,33,44]
a.remove(11) # it will remove ist time a value occur
# b=a.remove(44) it does not return a value
# 2nd method is   
a.remove(a[1])  # go and find the value present in the index 1 and remove it from the list a
print(a)

# print(b)

# pop(index)fun take index is an input and it return the value of passed index and remove
# it from the list
c=[11,22,33,11,44]
k=c.pop(3) # it will return value present at index 3 and remove it from the list
print("List = ", c)
print("Value of k = ", k) # value of k is remove from the list

j=[11,44,22,55,33,11,22]
print(j)

# sort() syntax.... listName.sort()
j.sort()# it will sort the list  ..note print(j.sort()) not work
print("Sort list = ", j)

# reverse() syntax...listName.reverse()
j.reverse()
print("Reverse List = ", j)

# count(value) fun will count how much time a value is repeat
# it return value for repeatetion of a value
print(j.count(11))
g=j.count(22)
print(f"the value {22} is repeat {g} times in the list")



