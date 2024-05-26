# Write a program that store the data in the dictionary is the prompt want

list=["a","b","c","d"]
dict={}
for k in list:
    print(f"Enter name that start with {k}")
    dict[k]=input().lower()

print("dictionary = ", dict)