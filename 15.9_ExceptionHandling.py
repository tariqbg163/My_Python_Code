# User Exception and user Handling except mechanism
age=22
try:
    if age<23:
        raise Exception("He/ She is teenage")
except Exception as e: # e is alias of Exception Class
    print("Exception = ", e) # user handld