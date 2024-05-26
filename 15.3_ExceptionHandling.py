# Multiple Exception block

print("enter numbers ")
try:
    a=eval(input(">> "))
    b=eval(input(">> "))
    print(a/b)
except TypeError:
    print("You enter invalid number")
except ZeroDivisionError:
    print("Invalid Division")
except ValueError:
    print("Value Error is found")
finally:
    print("it is final block")