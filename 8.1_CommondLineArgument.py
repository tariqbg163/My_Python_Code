from sys import argv
""" write a program that takes values from commond line and print the sum of
all the passed arguments  """
index=0
s=0
for k in argv:
    if index==0:
        index=1
    else:
        s=s+int(k)
print("Sum = ", s)