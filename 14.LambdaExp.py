# Lambda expression or anonymous fun(fu without name)
# Syntax .. lambdaKeyword arguments : single expression(return value)

# method one 
s=lambda a,b:a+b # it takes a and b and return a single expression value
k=s(11,22)
print(f"Value of k is {k}")

# Method two(2) for lambda expression or anonymous function
x=(lambda a,b:a+b) (11,12)
print(f"value of x is {x}")




# Lambda or anonymous function

tot = lambda  num1, num2 :  num1 +num2  # lambda function return a value to tot variable

total= tot(3,5)   # is the lambda fun have no name so we will call it through the variable  to which it return a value
print(f"Total = {total}")