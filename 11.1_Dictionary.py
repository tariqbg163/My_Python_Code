""" storing data in dictionary"""

d={1:"Mr khan", 2:"Kamal", 3:"jamal", "addrCode":4950}
print("d =", d)
# adding  data to dictionary
d[4]="Mr Shan" # this data is added b/c we have no key which is 4
print("after adding d =", d)

# updating value
d[1]="gul khan" # it will update the key 1 value
print("d = ",d)

for k in d:
    print("key =", k) # it will print the keys
    print("values =", d[k]) # it will print the values

