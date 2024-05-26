# Creating Global variable inside fun

def fun():
# If Global age is present outside it is will not create new age. it will use those 
# age variable. if not exist it will be created out side the method 
# it is mandatory to initialze the declare global variable inside that scope before use
    global age # take makes the age is global if age var exist ok else it will create it 
    age=20  # global age=23 gives error
    # we can over write its value
    print("Local variable inside fun  age= ", age)

fun()

print("Global variable outside fun age= ", age)