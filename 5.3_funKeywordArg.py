""" Keyword argument.. it is declare in the fun call time that which paramenter will 
receive its keyword value associated with it """

def sum(a,b,c):
    print("sum =",a+b+c)

sum(c=11, a=12,b=13) 
""" Note after keyword argument all the rest of argument comes
 will also be keyword argument """
    