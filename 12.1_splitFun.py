# entering multipule values from the user

# 1) by using multiple input() funs
# a,b=input("enter a "), input("enter b ")
# print("a =",a , " b=",b)

# 2) by using split(basedOn) fun base on space , ' ! etc split fun return a list
# Enter two numbers for the below code separated by space
a,b=input("enter a number ").split() # it will split the input on space
print("a =",a ," b=",b) # by default it is space

# split() we can pass space  , ' ; ! or any string character to split the input
# split() return a list of values

list1= input("enter number >> " , ) .split("/")
print("list1 = ", list1)

