"""
Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.
Examples
"1234123456785678" ➞ "************5678"
"8754456321113213" ➞ "************3213"
"35123413355523" ➞ "**********5523"
"""
card_hide = input("Enter card number please")
print ("*" * (len(card_hide)-4) + card_hide[-4:])