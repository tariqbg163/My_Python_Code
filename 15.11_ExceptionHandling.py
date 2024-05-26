# To create an object of exception class we have to create the class of it 
# we created our own exception class and try and handld(exception Mechanism)
class InsufficientBalance(ZeroDivisionError):
    def __init__(self, arg):
        self.msg=arg
    balance=5000
    with_d=int(input("Enter amount to withdraw = "))
    try:
        if balance<with_d:
            raise ZeroDivisionError("Insufficient Balance to withdraw from the account")
        balance=balance-with_d
    except ZeroDivisionError as e:
        print("Exception = ", e)
    finally:
        print("Current Balance = ", balance)
    
    