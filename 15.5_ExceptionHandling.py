# Except: message..  it handled everytype of exception class
# it always will not allow python to execute default exception mechanism
# Syntax is  exceptKeyword: Statement

print("Enter numbers ")
try:
    a=eval(input(">> ")) #eter "a","11", , : ; to execute except(2) block
    b=eval(input(">> "))
    print(a/b)
except (ZeroDivisionError,TypeError,ValueError):
    print("Invalid Operation")
except: # it will execute after above except block is not match
    print("it handled all types of exception")# it handled all types of exception
finally:
    print("It is final block")