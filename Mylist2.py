list1=[11,22,33,44,66,77,88,99]
# list1.remove(55) if value is not exit it crash the program
# rem=list1.remove(33)  remove fun can't return the removed element
# print("Removed element = ", rem)

list1.remove(33)  # pass the Element
print("List1 = ", list1)

# pop function is also used to remove element from the list
# pop return the removed element
removed=list1.pop()   # if no index is passed it remove the last index element
print("Remove Element is = ", removed)


rem=list1.pop(3) # remove the 3 index element from the list
print("Remove element = ", rem)
print("List1 = ", list1)

# delelte an element or a the list
list2=[11,22,33,44,55,66]
del list2[2]  # delete or remove the 2 index element
print("List2 = ", list2)

# del list2    it complete delete the list
# print("List2 = ",list2)


# clear() remove all the elements make the list empty []
list3=[11,222,33,44,55]
list3.clear()
print("List3 = ", list3)
