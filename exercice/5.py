"""
Create a function that takes a string and returns the number (count) of vowels contained within it.
Examples
"Celebration" ➞ 5
"Palm" ➞ 1
"Prediction" ➞ 4
Notes
a, e, i, o, u are considered vowels (not y).
"""
word = input()
# vowels = ("aeiou")
z = ((word.count("a"),word.count("e"), word.count("i"), word.count("o"), word.count("u") ))
print(sum(z))

