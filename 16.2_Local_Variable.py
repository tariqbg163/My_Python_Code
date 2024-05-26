# Local Variable--> Scope is limited to the function in which it is declare
def fun():
    age=21  # local vaiable
    print("Inside fun age= ", age)

fun()
    
# print("Ouside fun age= ", age) cause error b/c we are accessing local variable out of scope

def fun2(nm):  # nm is local variable
    name=nm  # name is local variable
    print("Inside fun Name = ", name)

fun2("Khan")
