# adding a single value to a set
s={11, 3.44, 55}
s.add(66)
print("Set =", s)

# Adding a sequence to a set
# Updating set by using update function
# update(sequence) and sequence is enclosed by [, ,] or (, , ,) or {, ,}
s.update((666,88)) 
print("Set again = ", s)

s.update([77,2222])
print("Set = ", s)

s.update({111,22244,4444})
print("set again = ",s)