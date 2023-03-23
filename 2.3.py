"""
Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.
Examples
5 ➞ True
-55 ➞ True
37 ➞ False
"""
our_nuber = int(input())
y = our_nuber % 5
if y == 0:
    print (True)
else:
    print (False)
    