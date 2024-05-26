# Set is unordered and unchangeable , ignore duplicate elements and take onces

s={11,22,33,44,11,22}
print("Set s = ", s)

# Creating set with set Contructor method 2 
s2= set((11,22,33,44,55,66)) # set([]),set({}), any sequence list,set,tuple, dictionary
print("Set s2 = ", s2)

# adding single element to set
s2.add("Khan")  # it the last location
print("Set s2 after adding Khan = ", s2)

# adding a sequence to the set usin update(sequence) i.e list,tuple, set, dictionary
s2.update(["cat", "dog",88])
print("Set s2 after update = ", s2) 

# remove(element) remove element from the set , if not exist raise error
s3={11,22,33,44,55,66}
s3.remove(22) # remove(21) raise error b/c it is not present in the set
print("S3 after remove =", s3)

# remove or discard element, discard(element), not raise error if not exist the element

s3.discard(21) # if not exist 
print("S3 after discard 21 = ", s3)

s3.discard(55)
print("S3 after dicard 55 = ", s3)

# pop , is also removing element it remove random element from the set 

s3.pop() # no index is required
print("S3 after pop = ", s3)
