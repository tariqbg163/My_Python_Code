# enter a list or sequenc from user
# the evalFun return values in (....) like a tuple
print("Enter a number")
b=eval(input(">> "))     # it can take, 55, 6.8  and "Ali Khan" in quotes
print(f"The value of b is {b}")

print("Enter a list")
list=[eval(x) for x in input().split("!")] # it separate the list element by !
print("List =", list)

# Note always use eval()fun if you want to type cast something 

# enter tuple from user
print("Enter values for tuple")                # elements by tuple is separated by ,
t=tuple([eval(k)  for k in input().split(",")]) # using tuple() constructor
print("tuple t= ",t)
print("enter values for set")
s=set([eval(j) for j in input().split(".")])
print("Set s= ",s)
