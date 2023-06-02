#30-Days-Of-Python Day 4 Levels 13 to 24
alphabet = 'abcdefghijklmnopqrstuvwxyz'
slice1 = alphabet[1:12:3]
print(slice1)

string = "Coding is For Everybody on Earth"

substring = 'Coding'

if string.startswith(substring):
    print("Yes it starts with Coding")

else:
    print("No it doesn't start with Coding")
    
substring2 = 'Coding'

if string.endswith(substring):
    print("Yes it ends with Coding")

else:
    print("No it doesn't end with Coding")
    
str = '  Coding For All  '
trim = str.strip()
print(trim)
