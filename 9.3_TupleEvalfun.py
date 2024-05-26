# Taking input for tuple from user 1)input()   2) eval() 

# 1) input function  and takes everything is an string
print("Enter number for tuple")
t=tuple(input()) # it consider each character and  space  is an element of  tuple
print(t)

# to remove , or space is an element from tuple drintking user input we use this method
print("Enter number of tuple")
t=eval(input()) # values must be separated by commas 22,44,55  or (23,24,55)
print(t)