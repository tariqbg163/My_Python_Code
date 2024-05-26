d={
    "Name":"Khan",
    "Age" :21,
    1850  :"postal_Code",
}
# it will update the existing values if not it a be added as a new keyValue Pair
d.update(name="Kamal", Age=22)  # single or sequnce of key value pair takes
print("D = ", d)
d.update(gender="Male", education="BSCS", cgpa=3.5)
print("after update d = ", d)
       # or below work same 
d.update({"Country":"Pakistan", "Age":25}) # single and multiple keyValuePair can be pass
# d.update({"Age":23})
print("d = ", d)

# del d["Age"]  # it will delete age keyValue Pair
# del d it completey delete the dictionary
# d.clear() it makes the dictionary empty {}

d2={"name":"Noor", "addres":"Baj", "P_code":1850}

pop_value=d2.pop("name")
print("Pop value = ", pop_value)

x=d2.popitem() # remove last or random item
print("PopItem = ", x)
