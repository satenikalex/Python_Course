"""
Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.
Examples
a,b = 9, 10 ➞ True
a,b = 9, 9 ➞ False
a,b = 1, 9 ➞ True


"""
a = int(input())
b = int(input())
if a or b == 10:
    print(True) 
elif a + b == 10:
    print (True)
else:
    print (False)
# + (a==0 or b==10) * True + (a+b==10) * True + (a> 10 and b> 10) * False
