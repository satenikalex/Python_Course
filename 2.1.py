"""
Emmy has written a function that returns a greeting to users. However, she's in love with Mubashir, and would like to greet him slightly differently. She added a special case in her function, but she made a mistake.
Can you help her?
Examples
"Matt" ➞ "Hello, Matt!"
"Helen" ➞ "Hello, Helen!"
"Mubashir" ➞ "Hello, my Love!"

"""
# input_name = input("Please enter your name")
# if input_name == "Mubashir":
#     print ("Hello, my love!")
# else:
#     print ("Hello," , input_name,"!")
# name =input("Enter name")
# y = "Hello, " + name
# x = "Hello, my Love!"
# x * name == "Mubashir"
# y * name != "Mubashir"
# print (x * (name == "Mubashir") + y * (name != "Mubashir"))
name = input()
res = name == "Mubashir"
print("Hello," + name * (not res) + "my Love!" * res)
