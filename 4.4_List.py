# adding all elements of a list
list=[11,22,33,44,55,66]
sum=0
k=0
while k<len(list):
    
    sum=sum+list[k]
    k=k+1
print("Sum of all elements of list is ", sum)
k=0
while k<len(list):
    if list[k]%2==0:
        print(f"the element {list[k]} is even")
    k=k+1