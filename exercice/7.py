"""
Create a function that replaces all the vowels in a string with a specified character.
Examples
"the aardvark", "#" ➞ "th# ##rdv#rk"
"minnie mouse", "?" ➞ "m?nn?? m??s?"
"shakespeare", "*" ➞ "sh*k*sp**r*"
"""
word = input()
# vowels = ("aeiou")

z = word.replace("a", "*") or  word.replace("e", "*") or word.replace("i", "*") or word.replace("o", "*") or word.replace("u","*" )
print(z)


