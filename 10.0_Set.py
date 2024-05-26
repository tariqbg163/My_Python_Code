s={11,22,33,11,22} # ignore duplicate items
print("Set =", s) # it not Mandatory to print the item in order which is created in set.

# Creating set from user using set() function

print("Enter value for set")
s=set(input())  # it consider every character is a single set element
print("S =", s)
"""  11,22,33  
S = {'3', '1', '2', ','}  b/c it consider 11 is reapted so it take 1 and take comma ,
ones b/c they are also repeated

"""

# s=set(111)   error will occur b/c it consider 111 is an object which is not iteratable
# print("S = ",s, " ", type(s))

s=set((11,22,33,44)) # it is sequence(iteratable)  it is ok
print("S = ", s)



