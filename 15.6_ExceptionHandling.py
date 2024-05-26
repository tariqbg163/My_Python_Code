# we can use else with except block .. it comes after except and before finally block
# it execute when no exception is araises. it execute before finally block

print("Enter number")
try:
    a=eval(input(">> ")) # enter numbers to execute the else part
    b=eval(input(">> ")) # Enter numbers to execute the else part
    print("Division of a/b = ",a/b)
except (ZeroDivisionError,ValueError,TypeError):
    print("Invalid Operation")
else: # it runs when no exception is occured
    print("No exception is occured")
finally:
    print("Mandatory code is in finally block")
    