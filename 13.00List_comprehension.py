
""" In Python, a list comprehension is a concise way to create lists. It provides a 
 compact syntax for creating a list by specifying the elements to be included within 
 square brackets []. The general syntax for a list comprehension is as follows:"""

""""
new_list = [expression for item in iterable if condition]
expression: The value you want to include in the new list.
item: The variable representing each element in the iterable (e.g., a list, range, etc.).
iterable: The sequence of elements to iterate over.
condition (optional): An optional condition that filters which elements to include in the
new list. """


squares = [x**2 for x in range(10)]
print(squares)

