#  We can delete(Remove) a value from a set is

j=s={11,22,33,44}
s.remove(44) # it remove but if not exist then it will cause error
print("set = ",s)

s.discard(22) # it will not cause error if value is not present
print("Again set = ", s)
