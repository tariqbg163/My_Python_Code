# Global Variable whose scope(life) is limited to program

age=22   # global variable
def fun():
    print("Global Var inside fun  Age = ", age)

fun()
print("Global Var ouside fun Age = ", age)
