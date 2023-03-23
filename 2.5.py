"""
Given a string, return True if its length is even or False if the length is odd.
"""
my_string = input()
length = int(len(my_string))
if length % 2 == 0:
    print (True)
else:
    print (False)