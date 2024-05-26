# adding a single value to a set
s={11,22}
s.add(33)
print("Set = ", s)

""" adding a sequence to a set . and sequence may be enclosed in (,,) or [] or {}
we use  update(sequence) function """ 
s.update([33,44]) # adding list to a set
print("set = ", s)
s.update((55,66)) # adding tuple to a set
print("set = ",s)

s.update({77,88}) # adding set to a set
print("set = ",s)

""" We can add multiple sequence to set i. update([],(),{}) or update((),())"""
k={11,22}
k.update((33,44),[55,66])  # update({66,77},{68,99})
print("set k =", k)


