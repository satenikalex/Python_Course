"""
Create a function to concatenate two integer lists.
Examples
[1, 3, 5], [2, 6, 8] ➞ [1, 3, 5, 2, 6, 8]
[7, 8], [10, 9, 1, 1, 2] ➞ [7, 8, 10, 9, 1, 1, 2]
[4, 5, 1], [3, 3, 3, 3, 3] ➞ [4, 5, 1, 3, 3, 3, 3, 3]
"""
list_1 = [7, 8]
list_2 = [10, 9, 1, 1, 2]
list_1.extend(list_2)
print(list_1)