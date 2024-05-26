age=22 # Global Variable
def fun():
    age=20  # local variable .. here it have high precedence
    print("inside fun age is = ", age)
    
    # Accessing Global variable inside fun when local and global variable have same name
    print("Global var inside fun = " , globals()["age"])

fun()

print("Global age = ", age) # it will access the Global Age variable