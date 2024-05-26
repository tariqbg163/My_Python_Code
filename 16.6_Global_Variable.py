age=22
print("Global age=s", age)
def fun():
    global age # take makes the age is global if age var exist ok else it will create it 
    age=20 # it will not create age it will use alredy age var is global variable
    print("Local variable inside fun  age= ", age)

fun()

print("Global variable outside fun age= ", age)