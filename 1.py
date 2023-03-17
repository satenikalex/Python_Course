"""
For this challenge, you are supposed to find the sum of the digits of a two-digit number.
45 ➞ 9
38 ➞ 11
67 ➞ 13
"""
def Sum(x):
    sum = 0
    for digit in str(x):
        sum += int(digit)
    return sum
x = 45
print(Sum(x))

