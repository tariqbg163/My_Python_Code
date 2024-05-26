print("Enter a number for length")
length=int(input(">>"))
list=[]
k=0
print(f"Enter {length} numbers for list")
while k<length:
    num=int(input(">>"))
    list=list+[num]
    k=k+1
print("List is = ", list)

maxValue=list[0] # suppose the index 0 is the smallest number
z=0
while z<length:
    if maxValue<list[z]:
        maxValue=list[z]
    z=z+1
print("Maximum Value= ", maxValue)
    
    
    