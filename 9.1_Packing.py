# Packing.. putting multiple values(variable) into a single variable
a=11
b=22
c=33

t=(a,b,c) # or t=a,b,c  we pack a,b,c into t tuple  ...  it is packing
print(t," ", type(t))

# unpacking is opposite of packing
t=(44,55,66)  

a,b,c=t  # we unpack the tuple 
print("a =",a, " ","b =",b," ", "c =", c)

#Note if tuple contain many elements then we use variablLength variable

t=(11,22,33,44,55,66,77)
a,b,c, *d=t   # d will receive the remaining tuple values
print("a =",)
print("b =",b)
print("c =",c)
print("d =",d)
