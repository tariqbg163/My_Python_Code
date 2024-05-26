# using else with loop ..it will execute 
# when the while loop condition is false or
# When the while loop is  completely executed i.e complete its iteration
# NOTE  else will not execute when while loop is terminate by break keyword

k=1
while k<5:
    print(k)
    k=k+1
else: # this else will execute when the while loop condition is become false
    print("while loop executed completely ???")
    
# else will not be execute when the loop is terminate by break keyword
j=1
while j<5:   # we can't use return in while  body
    if j==3:
        break
    print(j)
    j=j+1
else:# it will not execute if the loop is terminate by the break
    print("is else part is execute??")
    
print("...what happened...??") # not a part of while loop