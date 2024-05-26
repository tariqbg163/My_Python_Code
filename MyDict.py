# dictinary={key:value}  key=any type and value any type may be list tuple set, dictionary
d={
    "Name ": "Mr Khan",
    "Age  ": 21,
    "Gender":"Male",
}
print("Dictionary d = ", d)

# update(key=value), if key is not present it insert it is new element in dict
#d.update(Name="Shan Kamal", address="Peshawar")  # it will like "Name ":"Shan Kamal" and replace "Mr Khan"
# or 
d.update({"Addres":"Peshawar", 1850:"postal_Code"})

print("Dictionary d = ", d)

print("Name = ", d["Name"])

# updating element if exist  else it will take it is new element

d["Name"]="Noor Ahmad"      # updating exist element

# getting values through a specified key
print("Name =", d["Name"])  # or below
print("Name through getMethod = ", d.get("Name"))

d["Addres"]="Bajaur"      # updating i.e inserting new element to the dictionary
print("Addres = ", d["Addres"])
l=[11,22,33]

# retrive all keys of dictionary

d2={"Name":"Shan", "Age":21, 2024:"Year"}
a=d2.keys()  # it will return keys in list form
print("Keys of d = ", a)

# getting all values of a dictionary
values=d2.values()  # return a list of values
print("Values of d2 = ", values)

# dict.items() will return each item in a dictionary as tuple in a list
item= d2.items()
print("item(one keyValue pair) of d2 = ", item)





