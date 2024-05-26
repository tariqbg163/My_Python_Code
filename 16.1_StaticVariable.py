# Static Variable--> Class Variable, Shared Among object, no static keyword in python
class Test:
    age=22 # 1) Static variable.. same for all object,  class Variable
    def __init__(self, nm, college):
        self.name=nm   # instance variable
        Test.college=college  # 2) Static Variable
    def fun(self,ad,fee): # Instance Method can access static variable also
        self.address=ad # instance Variable
        Test.fee=fee  # 3) Static variable
    def show(self):
        print("Name=",self.name) # instance method
        print("Static Age = ", Test.age , "College = ",Test.college) # static method
           
    @staticmethod  # anotation is optional  , Mandatory if the take argument, no implicit arg
    def myStatic(): # static method .. con't access non static (instance) variable
        Test.gender="Male"          # 4) Static Variable, if exist override else create it
        print("Static Gender = " , Test.gender) 
        print("Static Fee = ", Test.fee)
        
    
    @classmethod  # Anotation Mandatory, implicitly take class object
    def funClass(cls):  # Class Method  which take class object is an argument
        Test.Board="BISE Malakand" # 5) Static Variable, if exit override else create it
        # Class Method have only Static Variable and can't access non static variable
        
t=Test("Khan","GPGC")
t.fun("Bajour", 60000)
t.show()
Test.Grade="A+"  # 6) Static variable
t.myStatic()
print("Instance Variables =",t.__dict__) # ref.__dict__ return dictionay of instanceVar
print("\n")
print("Static Variables   =",Test.__dict__)#class.__dict__ return dict of static variable

        
    
        