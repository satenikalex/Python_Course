1.
"""
Create a class with a few functions like these examples.

magic.replace("string", 'char', char') is a function that replaces all of the specified characters with different specified characters.
magic.str_length("string") is a function that returns the length of the string.
magic.trim(" string ") is a function that returns a string with truncated spaces at both the beginning and end.
magic.list_slice(list, tuple) is a function that returns the items in the list that are between the specified indexes. If the length of the new list is 0, return -1.
Examples
magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"

magic.str_length("hello world") ➞ 11

magic.trim("      python is awesome      ") ➞ "python is awesome"

magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]
"""
# class Magic:
#     def replace(string, char1, char2):
#         return string.replace(char1, char2)
#     def str_length(string):
#         return len(string)
#     def trim(string):
#         return string.strip()
#     def list_slice(list, tuple):
#         return list[tuple[0]:tuple[1]]

# print(Magic.replace("AzErty-QwErty", "E", "e"))

# class Magic:
#     @staticmethod
#     def replace(string, char_to_replace, replacement_char):
#         return string.replace(char_to_replace, replacement_char)

#     @staticmethod
#     def str_length(string):
#         return len(string)

#     @staticmethod
#     def trim(string):
#         return string.strip()

#     @staticmethod
#     def list_slice(lst, index_range):
#         start, end = index_range
#         sliced_list = lst[start:end + 1]
#         return sliced_list if sliced_list else -1
2.
"""
Ones, Threes and Nines (Version #2)
Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string in this format:

"nines:your answer, threes:your answer, ones:your answer"
You need to find out how many ones, threes, and nines it would at least take for the number of each to add up to the given integer when multiplied by one, three or nine (depends).

Examples
ones_threes_nines(10) ➞ "nines:1, threes:0, ones:1"

ones_threes_nines(15) ➞ "nines:1, threes:2, ones:0"

ones_threes_nines(22) ➞ "nines:2, threes:1, ones:1"

"""
# class Magic:
#     def __init__(self):
#         self.answer = ""

#     def ones_threes_nines(self, num):
#         nines = num // 9
#         num %= 9
#         threes = num // 3
#         num %= 3
#         ones = num

#         self.answer = f"nines:{nines}, threes:{threes}, ones:{ones}"

#         return self.answer
# magic = Magic()
# print(magic.ones_threes_nines(22))
3.
"""
To the Right, to the Right!
Create a class that imitates a select screen. For simplicity, the cursor can only move right!

In the display method, return a string representation of the list, but with square brackets around the currently selected element. Also, create the method to_the_right, which moves the cursor one element to the right.

The cursor should start at index 0.

Examples
menu = Menu([1, 2, 3])
menu.display() ➞ "[[1], 2, 3]"
menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"
"""
# class SelectScreen:
#     def __init__(self, elements):
#         self.elements = elements
#         self.cursor = 0

#     def display(self):
#         result = ""
#         for i, element in enumerate(self.elements):
#             if i == self.cursor:
#                 result += f"[{element}] "
#             else:
#                 result += f"{element} "
#         return result.strip()

#     def to_the_right(self):
#         self.cursor = (self.cursor + 1) % len(self.elements)
# screen = SelectScreen(["Option 1", "Option 2", "Option 3", "Option 4"])
# print(screen.display())  

# screen.to_the_right()
# print(screen.display())  

# screen.to_the_right()
# print(screen.display())  

# screen.to_the_right()
# print(screen.display())  

# screen.to_the_right()
# print(screen.display())  
4
"""Employee Parsing
In the class Employee, implement the instance attributes as firstname, lastname and salary.

Create the method from_string() which parses a string containing these attributes and assigns them to the correct properties. Properties will be separated by a dash.

Examples
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
emp1.firstname ➞ "Mary"

emp1.salary ➞ 60000

emp2.firstname ➞ "John"

emp2.salary ➞ 55000
"""
# class Employee:
# 	def __init__(self, first, last, salary):
# 		self.firstname = first
# 		self.lastname = last
# 		self.salary = salary
# 	def from_string(s):
# 		s = s.split('-')
# 		return Employee(s[0],s[1],int(s[2]))
5
"""
People Sort
Given a list of people objects, create a function that sorts the list by an attribute name. The attribute to sort by will be given as a string.

The Person class will only include these attributes in the following order:

firstname
lastname
age
Examples
p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
people_sort([p1, p2, p3], "firstname") ➞ [p2, p1, p3]
# Alice, Michael, Zoey

people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
# Jones, Smith, Waters

people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
"""
"""
Առաջին եղանակ
"""
# class Employee:
 
#     def __init__(self, name, dept, age):
#         self.name = name
#         self.dept = dept
#         self.age = age
 
#     def __repr__(self):
#         return '{' + self.name + ', ' + self.dept + ', ' + str(self.age) + '}'
 
# if __name__ == '__main__':
 
#     employees = [
#         Employee("Michael", "Smith", 40),
#         Employee("Alice", "Waters", 21),
#         Employee("Zoey", "Jones", 29)
#     ]
 
#     employees.sort(key=lambda x: x.name)
 
#     print(employees)
 
#     employees.sort(key=lambda x: x.name, reverse=True)
 
#     print(employees)    
"""
2-րդ եղանակ առանց class-ի
"""
# def people_sort(lst, attr):
#     if attr == "age":
#          return sorted(lst, key=lambda item: item.age)
#     elif attr == "firstname":
#         return sorted(lst, key=lambda item: item.firstname)
#     else:
#          return sorted(lst, key=lambda item: item.lastname)
6
"""
Wait... Who Am I?
Hello there, I... seem to not remember who I am, my memories is all... cloudy, although maybe if I could piece it together...

Oh! Maybe you could help me make a class that helps me remember things. Maybe a method called add that would add to my memory if I would recall things and a remember method that would let me recall a specific memory.

But you have to make add more flexible, I might recall many things in an instant or only one that I would forget again.

Examples :D
# add method doesn't return anything.
memories.add(name="Shane", gender="M", catch_phrase="bazinga")

memories.add(work="None", love_life=0)

memories.add(adress="car")

memories.remember("work") ➞ "None"

memories.remember("gender") ➞ "M"

# If memory was not added, return False
memories.remember("lover") ➞ False
"""
# class Memories:
#     def __init__(self):
#         self.memory = {}

#     def add(self, **kwargs):
#         self.memory.update(kwargs)

#     def remember(self, key):
#         return self.memory.get(key, False)
# memories = Memories()

# memories.add(name="Shane", gender="M", catch_phrase="bazinga")
# memories.add(work="None", love_life=0)
# memories.add(address="car")

# print(memories.remember("work"))  
# print(memories.remember("gender"))  
# print(memories.remember("lover"))  
7
"""
Shiritori Game
This challenge is an English twist on the Japanese word game Shiritori. The basic premise is to follow two rules:

First character of next word must match last character of previous word.
The word must not have already been said.
Below is an example of a Shiritori game:

["word", "dowry", "yodel", "leader", "righteous", "serpent"]  #valid!

["motive", "beach"]  # invalid! - beach should start with "e"

["hive", "eh", "hive"]  # invalid! - "hive" has already been said
Write a Shiritori class that has two instance variables:

words: a list of words already said.
game_over: a boolean that is true if the game is over.
and two instance methods:

play: a method that takes in a word as an argument and checks if it is valid (the word should follow rules #1 and #2 above).

If it is valid, it adds the word to the words list, and returns the words list.
If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to true.
restart: a method that sets the words list to an empty one [] and sets the game_over boolean to false. It should return "game restarted".

Examples
my_shiritori = Shiritori()

my_shiritori.play("apple") ➞ ["apple"]
my_shiritori.play("ear") ➞ ["apple", "ear"]
my_shiritori.play("rhino") ➞ ["apple", "ear", "rhino"]
my_shiritori.play("corn") ➞ "game over"

# Corn does not start with an "o".

my_shiritori.words ➞  ["apple", "ear", "rhino"]

# Words should be accessible.

my_shiritori.restart() ➞ "game restarted"
my_shiritori.words ➞ []

# Words list should be set back to empty.

my_shiritori.play("hostess") ➞ ["hostess"]
my_shiritori.play("stash") ➞ ["hostess", "stash"]
my_shiritori.play("hostess") ➞ "game over"

# Words cannot have already been said.
"""
# class Shiritori:
#     def __init__(self):
#         self.words = []
#         self.game_over = False

#     def play(self, word):
#         if not self.words or self.words[-1][-1] == word[0] and word not in self.words:
#             self.words.append(word)
#             return self.words
#         else:
#             self.game_over = True
#             return "game over"

#     def restart(self):
#         self.words = []
#         self.game_over = False
#         return "game restarted"
# my_shiritori = Shiritori()

# print(my_shiritori.play("apple")) 
# print(my_shiritori.play("ear"))  
# print(my_shiritori.play("rhino"))  
# print(my_shiritori.play("corn"))  
# print(my_shiritori.words)  
# print(my_shiritori.restart())  
# print(my_shiritori.words)  
# print(my_shiritori.play("hostess"))  
# print(my_shiritori.play("stash"))  
# print(my_shiritori.play("hostess")) 
8.
"""
Employee Class with Keywords
Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. Each instance should have a name and a lastname attribute plus one more attribute for each of the keywords, if any.

Examples
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

john.name ➞ "John"
mary.lastname ➞ "Major"
richard.height ➞ 178
giancarlo.nationality ➞ "Italian"
"""
class Employee:
    def __init__(self, full_name, **kwargs):
        self.name, self.lastname = full_name.split()
        for key, value in kwargs.items():
            setattr(self, key, value)
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
