def sum(a=0, b=1, c=2): # it ist positional and then detault arguments
    print("Sum = ",a+b+c)

sum() # it will take default value
sum(22) # a=22 and other will take default value
sum(10,20) # a=10, b=20 and c will take default value
sum(10,20,30) # it takes a=10, b=20, c=30
""" value is according the order in which they are decalre sum(11) will be the first
positional argument value which is (a) and so on
2) it is the user responsibility to pass a value to sum if the take a value i.e
sum(a,b) if sum(10) then eror occur b/c b is not receiving any value ..to remove such a
problem we use default value argument i.e sum(a, b=20) if sum(10) it will work """