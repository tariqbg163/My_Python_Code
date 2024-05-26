# enter a data from user .. split() fun always return a list
print("Enter today date")

# date=int(input().split('/')) this style is getting error b/c we can not list to int 
# print("Date =",date)  by int() function 

date=[int(x) for x in input().split("/")] # split() fun return a list
print("Date =", date)

# Remember
a,b,c=[11,12,13]
print(a , b, c)

