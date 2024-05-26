# user try and user except

balance=6000
with_d=int(input("Enter amount to withdraw = "))
try:
    if balance<with_d:
        raise ArithmeticError("Insufficient balance to withdraw from account")
    balance=balance-with_d
except ArithmeticError as ar: # ar is alias for ArithmeticError
    print("Exception = ", ar)
finally:
    print("Current Balance is ", balance)
    