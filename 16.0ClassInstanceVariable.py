# Instance variable is associated with objects. Three ways to create an instance variable
#  1) __init__(self),    (2) methods(self),    (3) outside class(i.e obj.varName)

class MyClass:
    
    def __init__(self, ag, nm):  # 1) method to create an instance variable , instance method
        self.age=ag             # instance variable
        self.name=nm            # instance variable
    
    def fun(self, ad):  # 2) Method of creating instance variable  instance method
        self.address=ad  # instanc variable
        
    def show(self):  # instance method
        print(f"My name is {self.name} address {self.address} and  age is {self.age}")
    
obj=MyClass(21,"Mr Khan")  # it is actually like MyClass(obj,21, "Mr Khan")

obj.fun("Bajaur")  # instance method b/c it is call with object(reference)
obj.show()         # instance method

# 3) method of creating instance variable which is outside the class

obj.gender="Male"   # ref_Var.instance_Var_Name
print("Gender =" ,obj.gender)

        