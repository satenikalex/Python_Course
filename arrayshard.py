""" ARRAYS HARD"""
1
# def interview(time_taken_list, total_time_taken):
#     # Check if the candidate has completed all the questions
#     if len(time_taken_list) != 8:
#         return "disqualified"

#     # Check if the total time taken is within the allowed limit
#     if total_time_taken > 120:
#         return "disqualified"

#     # Check if the time taken for each question is within the allowed limits
#     for i in range(len(time_taken_list)):
#         if i < 2:  # Very easy questions
#             if time_taken_list[i] > 5:
#                 return "disqualified"
#         elif i < 4:  # Easy questions
#             if time_taken_list[i] > 10:
#                 return "disqualified"
#         elif i < 6:  # Medium questions
#             if time_taken_list[i] > 15:
#                 return "disqualified"
#         else:  # Hard questions
#             if time_taken_list[i] > 20:
#                 return "disqualified"

#     # If all conditions are satisfied, return "qualified"
#     return "qualified"

# result = interview([5, 5, 10, 10, 15, 15, 20, 20], 120)
# print(result)  # Output: "qualified"
# 2
# def rep_set(n):
#     if n == 0:
#         return []
#     else:
#         prev_set = rep_set(n - 1)
#         return prev_set + [prev_set]

# # Examples
# print(rep_set(0))  # Output: []

# print(rep_set(1))  # Output: [[]]

# print(rep_set(2))  # Output: [[], [[]]]

# print(rep_set(3))  # Output: [[], [[]], [[], [[]]]]
3
# def arithmetic_operation(s):
#     s = s.split()
#     num1 = int(s[0])
#     operator = s[1]
#     num2 = int(s[2])

#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '//':
#         if num2 == 0:
#             return -1
#         else:
#             return num1 // num2
#     else:
#         return None  # Invalid operator

# # Examples
# print(arithmetic_operation("12 + 12"))  # Output: 24
# print(arithmetic_operation("12 - 12"))  # Output: 0
# print(arithmetic_operation("12 * 12"))  # Output: 144
# print(arithmetic_operation("12 // 0"))  # Output: -1
4.
# def encode_morse(string):
#     char_to_dots = {
#         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#         'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#         '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#         '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#         ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#         '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
#     }

#     morse_code = []
#     for char in string:
#         upper_char = char.upper()
#         if upper_char in char_to_dots:
#             morse_code.append(char_to_dots[upper_char])

#     return ' '.join(morse_code)

# # Examples
# print(encode_morse("EDABBIT CHALLENGE"))  # Output: ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
# print(encode_morse("HELP ME !"))  # Output: ".... . .-.. .--.   -- .   -.-.--"
5.
# def mahjong_tiles():
#     ranks = ['yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
#     suits = ['tong', 'tiao', 'wan']
#     special_tiles = {
#         '1tong': 'bing gan',
#         '2tong': 'yan jing',
#         '1tiao': 'ji'
#     }

#     tiles = []

#     # Generate regular tiles
#     for rank in ranks:
#         for suit in suits:
#             tiles.append(rank + ' ' + suit)

#     # Substitute special tiles
#     for tile, special_name in special_tiles.items():
#         tiles = [special_name if x == tile else x for x in tiles]

#     # Duplicate tiles to have 4 copies
#     tiles *= 4

#     return tiles

# # Example usage
# tiles = mahjong_tiles()
# for tile in tiles:
#     print(tile)
6
# def consecutive_combo(lst1, lst2):
#     combined_lst = lst1 + lst2
#     combined_lst.sort()

#     for i in range(1, len(combined_lst)):
#         if combined_lst[i] != combined_lst[i-1] + 1:
#             return False

#     return True

# # Examples
# print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))  # Output: True
# print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))  # Output: False
# print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))  # Output: False
# print(consecutive_combo([44, 46], [45]))  # Output: True
7
# def tallest_skyscraper(skyline):
#     max_height = 0
#     rows = len(skyline)
#     cols = len(skyline[0])

#     for col in range(cols):
#         height = 0
#         for row in range(rows):
#             if skyline[row][col] == 1:
#                 height = rows - row
#                 break
#         if height > max_height:
#             max_height = height

#     return max_height

# # Examples
# print(tallest_skyscraper([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]))  # Output: 3
# print(tallest_skyscraper([[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]))  # Output: 4
# print(tallest_skyscraper([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]))  # Output: 2
8
# def sock_merchant(socks):
#     sock_count = {}
#     pair_count = 0

#     for sock in socks:
#         sock_count[sock] = sock_count.get(sock, 0) + 1

#     for count in sock_count.values():
#         pairs = count // 2
#         pair_count += pairs

#     return pair_count

# # Examples
# print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))  # Output: 3
# print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))  # Output: 4
# print(sock_merchant([]))  # Output: 0
9
# def remove_letters(lst, string):
#     letters_to_remove = set(string)
#     result = []

#     for letter in lst:
#         if letter not in letters_to_remove:
#             result.append(letter)

#     return result

# # Examples
# print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))  # Output: ["w"]
# print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))  # Output: ["b", "g", "w"]
# print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))  # Output: []
10
# def majority_vote(lst):
#     if len(lst) == 0:
#         return None

#     vote_count = {}

#     for element in lst:
#         if element in vote_count:
#             vote_count[element] += 1
#         else:
#             vote_count[element] = 1

#     for element, count in vote_count.items():
#         if count > len(lst) / 2:
#             return element

#     return None

# # Examples
# print(majority_vote(["A", "A", "B"]))  # Output: "A"
# print(majority_vote(["A", "A", "A", "B", "C", "A"]))  # Output: "A"
# print(majority_vote(["A", "B", "B", "A", "C", "C"]))  # Output: None
11
# def pluralize(lst):
#     word_counts = {}
#     for word in lst:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
    
#     plural_words = set()
#     for word, count in word_counts.items():
#         if count > 1:
#             plural_words.add(word + "s")
#         else:
#             plural_words.add(word)
    
#     return plural_words
12
# def secret(txt):
#     classes = txt.split(".")[1:]  # Extract class names, excluding the first element
    
#     class_attr = " ".join(classes)  # Join class names with spaces
    
#     return f"<{txt} class='{class_attr}'></{txt}>"
# print(secret("p.one.two.three"))
# # Output: "<p class='one two three'></p>"

# print(secret("p.one"))
# # Output: "<p class='one'></p>"

# print(secret("p.four.five"))
# # Output: "<p class='four five'></p>"
13
# import math

# def distance(point1, point2):
#     x1, y1 = point1
#     x2, y2 = point2
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# def perimeter(points):
#     side1 = distance(points[0], points[1])
#     side2 = distance(points[1], points[2])
#     side3 = distance(points[2], points[0])
    
#     return round(side1 + side2 + side3, 2)
# print(perimeter([[15, 7], [5, 22], [11, 1]]))
# # Output: 47.08

# print(perimeter([[0, 0], [0, 1], [1, 0]]))
# # Output: 3.41

# print(perimeter([[-10, -10], [10, 10], [-10, 10]]))
# # Output: 68.28
14
# def count_datatypes(*args):
#     type_counts = [0, 0, 0, 0, 0, 0]  # Initialize the counts for each data type
    
#     for arg in args:
#         if isinstance(arg, int):
#             type_counts[0] += 1
#         elif isinstance(arg, str):
#             type_counts[1] += 1
#         elif isinstance(arg, bool):
#             type_counts[2] += 1
#         elif isinstance(arg, list):
#             type_counts[3] += 1
#         elif isinstance(arg, tuple):
#             type_counts[4] += 1
#         elif isinstance(arg, dict):
#             type_counts[5] += 1
    
#     return type_counts
# print(count_datatypes(1, 45, "Hi", False))
# # Output: [2, 1, 1, 0, 0, 0]

# print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))
# # Output: [3, 0, 0, 1, 1, 0]

# print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23))
# # Output: [2, 2, 3, 1, 0, 2]

# print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]))
# # Output: [2, 0, 1, 2, 2, 0]
15
def unique_styles(albums):
    unique_styles_set = set()

    for album in albums:
        styles = album.split(",")
        unique_styles_set.update(styles)

    return len(unique_styles_set)
print(unique_styles([
    "Dub,Dancehall",
    "Industrial,Heavy Metal",
    "Techno,Dubstep",
    "Synth-pop,Euro-Disco",
    "Industrial,Techno,Minimal"
]))
# Output: 9

print(unique_styles([
    "Soul",
    "House,Folk",
    "Trance,Downtempo,Big Beat,House",
    "Deep House",
    "Soul"
]))
# Output: 7

