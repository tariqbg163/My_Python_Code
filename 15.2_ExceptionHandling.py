# finally execution order
# if no exception araise then try--->finally direct execute
# if exception occur and except block match  then try--->exceptBlock-->finally block
# if exception occur and except block not match then try-->finally-->default execpt block

print("enter numbers ")
try:    # enter two number to check the order 1
    a=eval(input(">> ")) # enter b is 0 to check the order 2
    b=eval(input(">> ")) # enter any character(not number and 0) to check order 3
    print(a/b)
except ZeroDivisionError:
    print("Invalid denamenator 0")
finally:
    print("finall block is executed")