# multi variable length parameter
# syntax is *variableName

#to declare a function which will receive any number of arguments and make its sum
def sum(*num):
    sm=0
    for k in num:
        sm=sm+k
    return sm
#we can call the sum with any number of arguments
totalSum=sum(11,22,33)
print("Total sum = ", totalSum)

# lets call the sum function with two arguments
totalSum=sum(11,22)
print(f"Total sum is {totalSum}")
""" Note..
1) Positional arguments is comes first and then after is default argument 
can occur in a single function

e.t  fun(Positional, default, variableLengthArgument) it is true

2) fun(defaultArgument, positionalArgumetn) error occur 
    but fun(Positional , defaultArguments) it is true
    
3) fun(default, *VariableLengtheArguement)  it is true   
    but fun(variableLenghtArgument, default) error occur

4)fun(positional, VariableLengthArgument) it is True
  but  fun(VariableLengthArgument, positional)  error occur
  """