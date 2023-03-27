"""
Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.
Examples
[5, 57] ➞ True
[77, 30] ➞ False
[0] ➞ True
"""
my_list = [77, 30]
z = sum(my_list) 
print ((z < 100) * "True", (z >= 100) * "False")
