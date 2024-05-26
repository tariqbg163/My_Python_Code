# exception object is raise by python and Handled by user except Mechanism
# When user exception block is execute program run successfully without crash
# Default try(raise) and user except mechanism

a=eval(input("enter a number>> "))
b=eval(input("enter a number>> "))
try:
    x=a/b # default raise
    print("is exception is occure")
except ZeroDivisionError:  # user except mechanism ..program will run successfully
    print("Exception happened")
finally:#It's optional.It comes after except. If no except then if comes after try
    print("Finall always execute and it is optional")
    # it will always execute wether exception is occured or not.
    #it mostly occur after except block in no except bloct then after try finally occur

print("Program Continue...")