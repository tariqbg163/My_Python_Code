list=[11,22,33]
# print(list[3]) when we try to access index out of range it cause error

# list[3]=44 we can't update an index which is out of range
# print(list)

# adding two list
l1=[11,22,33]
l2=[44,55,66]
l3=l1+l2  # list1 and list2 will merge in list3 , _,*,%, / is not possible in case of list , + is for concatenation
print("List3 =", l3)
# comparing two list
print(l1==l2)

"""  we can't add a scaler (single value) to list b/c it is collection
l1=[11,22] +4
print(l1)  but   l1=[11,22]+[4] it true b/c now [4] is single value list i.e """
l1=[11,22] + [4]
print("List1 =", l1)

""" Multiplying a list with scaler is possible and while repeat the list element
by the number of time with which it is multiplied  i.e l1=[11,22] *4 will repeat
[11,22,11,22,11,22,11,22] times """
l1=[11,22]*4   # + , _ , %, / is not possible
print(l1)

""" Compound Assingnment Operator  in list
l=[11,22] 
1=l+[10]  and its compound Assingnment Operator is 
l+=[10]   same of multiplication e.g
"""
l=[11,22]
l+=[33]    # + , _ , %, / is not possible
print("List l =",l)

