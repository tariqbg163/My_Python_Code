# Mutiple exception using one except block

print("enter numbers")
try:
    a=eval(input(">> "))
    b=eval(input(">> "))
    print(a/b)
except (ZeroDivisionError,TypeError,ValueError):
    print("Invalid operation")
finally:
    print("It's finally block")