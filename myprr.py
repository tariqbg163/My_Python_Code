# li=[]
# li.append("Ali")
# li.append(123)
# print(li[1])
# print(li)
# li.insert(0,"Ahmad")
# li.insert(1,333)
# print(li)

# li.remove(li[0])
# li.remove(123)
# print(li)

# li.insert(1,323)
# li.append(876)
# print(li)

# num=li.pop(1)
# print(num)
# print(li)


# ar=[11,22,33,44,55,66,11,22,44,44,55,44]
# print(ar.count(44))

# print(ar.sort())

# ar=[]
# print("Enter the length for the list")
# length= int(input(">>  ", ))
# index=0
# print("Enter only intigers ! ")
# while (index <= length):
#     element=int(input(">> " ,))
#     if(type((element))==int):
#         ar=ar + [element]
#     else:
#         print("You enterd invalid number ")
#     index =index +1

# --______________________________________________________________________________

# Ternary Operator   ... it is used to assign a value to a variable
# num1=22
# num2=33

# num = num1 if num1 > num2 else num2
# print(f'num is {num}')


# ______________________________________________________________________________________________

# Dictionary Comprehension

# creating run time dictionary 
# dict_1 = {key:eval(input()) for key in range(4)}
# print(f"Dictionary_1 = {dict_1}")

# ________________________________________________________________________________________________

# Lambda or anonymous function

# tot = lambda  num1, num2 :  num1 +num2  # lambda function return a value to tot variable

# total= tot(3,5)   # is the lambda fun have no name so we will call it through the variable  to which it return a value
# print(f"Total = {total}")

# _________________________________________________________________________________________

# Exception Handling in Python

num1 = eval(input("Enter num1 >> "))
num2 = eval(input("Enter num2 >> "))

try:
    num = num1 / num2
    # print(f" num = {num}")  # successfully divided
except ZeroDivisionError as zr:
    print(zr)




print(f"num = {num}")
